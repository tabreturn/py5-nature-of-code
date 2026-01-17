# brain_ga.py
from __future__ import annotations

import math
import random
from typing import List


def _tanh(x: float) -> float:
    return math.tanh(x)


def _sigmoid(x: float) -> float:
    # stable enough for our small numbers
    return 1.0 / (1.0 + math.exp(-x))


class Brain:
    """
    Fixed-topology neural net:
      4 inputs -> H hidden -> 1 output
    Evolved with a simple GA (crossover + mutation).
    """

    def __init__(self, num_inputs: int = 4, num_hidden: int = 8) -> None:
        self.n_in = num_inputs
        self.n_h = num_hidden

        # weights:
        # input->hidden: n_h * n_in
        # hidden bias:   n_h
        # hidden->out:   n_h
        # out bias:      1
        self.w_ih = [random.uniform(-1.0, 1.0) for _ in range(self.n_h * self.n_in)]
        self.b_h = [random.uniform(-1.0, 1.0) for _ in range(self.n_h)]
        self.w_ho = [random.uniform(-1.0, 1.0) for _ in range(self.n_h)]
        self.b_o = random.uniform(-1.0, 1.0)

    def copy(self) -> "Brain":
        b = Brain(self.n_in, self.n_h)
        b.w_ih = self.w_ih[:]
        b.b_h = self.b_h[:]
        b.w_ho = self.w_ho[:]
        b.b_o = self.b_o
        return b

    def predict_flap(self, inputs: List[float]) -> bool:
        """Return True if we should flap."""
        if len(inputs) != self.n_in:
            raise ValueError(f"Expected {self.n_in} inputs, got {len(inputs)}")

        # hidden activations
        h = []
        for j in range(self.n_h):
            s = self.b_h[j]
            base = j * self.n_in
            for i in range(self.n_in):
                s += self.w_ih[base + i] * inputs[i]
            h.append(_tanh(s))

        # output
        s_out = self.b_o
        for j in range(self.n_h):
            s_out += self.w_ho[j] * h[j]

        # classification-like decision (probability-ish)
        p = _sigmoid(s_out)
        return p > 0.5

    @staticmethod
    def crossover(a: "Brain", b: "Brain") -> "Brain":
        """Per-weight uniform crossover."""
        if (a.n_in, a.n_h) != (b.n_in, b.n_h):
            raise ValueError("Brain shapes do not match")

        child = Brain(a.n_in, a.n_h)

        child.w_ih = [random.choice([wa, wb]) for wa, wb in zip(a.w_ih, b.w_ih)]
        child.b_h = [random.choice([wa, wb]) for wa, wb in zip(a.b_h, b.b_h)]
        child.w_ho = [random.choice([wa, wb]) for wa, wb in zip(a.w_ho, b.w_ho)]
        child.b_o = random.choice([a.b_o, b.b_o])

        return child

    def mutate(self, rate: float = 0.01, sigma: float = 0.5) -> None:
        """Like JS: child.mutate(0.01). Adds gaussian noise to some weights."""
        def maybe_mut(x: float) -> float:
            if random.random() < rate:
                return x + random.gauss(0.0, sigma)
            return x

        self.w_ih = [maybe_mut(x) for x in self.w_ih]
        self.b_h = [maybe_mut(x) for x in self.b_h]
        self.w_ho = [maybe_mut(x) for x in self.w_ho]
        self.b_o = maybe_mut(self.b_o)

