from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, List, Dict
import math
import neat

# ============================================================
# NEAT CONTEXT (ml5-style hidden state)
# ============================================================

_CURRENT_GENOME = None
_CURRENT_CONFIG = None


def set_current_neat(genome, config) -> None:
    """Set the genome/config used by Bird() during construction."""
    global _CURRENT_GENOME, _CURRENT_CONFIG
    _CURRENT_GENOME = genome
    _CURRENT_CONFIG = config


def get_current_neat():
    if _CURRENT_GENOME is None or _CURRENT_CONFIG is None:
        raise RuntimeError(
            "NEAT context not set. "
            "Call set_current_neat(genome, config) before creating Bird()."
        )
    return _CURRENT_GENOME, _CURRENT_CONFIG


# ============================================================
# NEAT → ml5-like BRAIN WRAPPER
# ============================================================

def _sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


@dataclass
class NeatBrain:
    # ml5-style metadata (parity only)
    inputs: int
    outputs: Sequence[str]
    task: str = "classification"
    neuroEvolution: bool = True

    # actual NEAT network
    net: object | None = None

    @classmethod
    def create(
        cls,
        *,
        inputs: int,
        outputs: Sequence[str],
        task: str,
        neuroEvolution: bool,
    ) -> "NeatBrain":
        """
        Create a brain using the *current* NEAT genome/config.
        Mirrors ml5.neuralNetwork({...}) as closely as possible.
        """
        genome, config = get_current_neat()

        net = neat.nn.FeedForwardNetwork.create(genome, config)

        # Safety checks (fail early, fail loud)
        if config.genome_config.num_inputs != inputs:
            raise ValueError("NEAT num_inputs does not match brain.inputs")

        if config.genome_config.num_outputs not in (1, len(outputs)):
            raise ValueError("NEAT num_outputs incompatible with outputs")

        return cls(
            inputs=inputs,
            outputs=tuple(outputs),
            task=task,
            neuroEvolution=neuroEvolution,
            net=net,
        )

    def classifySync(self, inputs: List[float]) -> List[Dict[str, float | str]]:
        if self.net is None:
            raise RuntimeError("NeatBrain has no network")

        out = self.net.activate(inputs)

        # 1-output neuron → threshold
        if len(out) == 1:
            p = _sigmoid(out[0])
            label = self.outputs[0] if p > 0.5 else self.outputs[1]
            conf = p if label == self.outputs[0] else 1 - p
            return [{"label": label, "confidence": conf}]

        # 2-output neurons → argmax
        i = max(range(len(out)), key=lambda k: out[k])
        return [{"label": self.outputs[i], "confidence": out[i]}]