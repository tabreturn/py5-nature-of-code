# ml5.js-style neural network functionality implemented with bespoke class.

from __future__ import annotations
from py5 import np

_rng = np.random.default_rng()


class Brain:
    """Vectorized NumPy brain with GA helpers."""

    def __init__(self, inputs: int, outputs: int, hidden: int = 8) -> None:
        self.n_in, self.n_h, self.n_out = inputs, hidden, outputs
        self.w_ih = _rng.uniform(-1.0, 1.0, (hidden, inputs))
        self.b_h = _rng.uniform(-1.0, 1.0, (hidden,))
        self.w_ho = _rng.uniform(-1.0, 1.0, (outputs, hidden))
        self.b_o = _rng.uniform(-1.0, 1.0, (outputs,))

    def forward(self, inputs: list[float]) -> list[float]:
        x = np.asarray(inputs, dtype=float)
        h = np.tanh(self.w_ih @ x + self.b_h)
        return (self.w_ho @ h + self.b_o).tolist()

    # Classify and prediction methods.

    def classify_binary(self, inputs: list[float], threshold: float = 0.5) -> bool:
        z = self.forward(inputs)[0]
        p = 1.0 / (1.0 + np.exp(-z))
        return p > threshold

    def predict_continuous_01(self, inputs: list[float]) -> list[float]:
        raw = np.asarray(self.forward(inputs), dtype=float)
        return ((np.tanh(raw) + 1.0) * 0.5).tolist()

    # Crossover and mutation.

    def crossover(self, other: 'Brain') -> 'Brain':
        c = Brain(self.n_in, self.n_h, self.n_out)
        c.w_ih = np.where(_rng.random(self.w_ih.shape) < 0.5, self.w_ih, other.w_ih)
        c.b_h = np.where(_rng.random(self.b_h.shape) < 0.5, self.b_h, other.b_h)
        c.w_ho = np.where(_rng.random(self.w_ho.shape) < 0.5, self.w_ho, other.w_ho)
        c.b_o = np.where(_rng.random(self.b_o.shape) < 0.5, self.b_o, other.b_o)
        return c

    def mutate(self, rate: float = 0.01, sigma: float = 0.5) -> None:
        def mut(arr: np.ndarray) -> np.ndarray:
            m = _rng.random(arr.shape) < rate
            return arr + m * _rng.normal(0.0, sigma, arr.shape)

        self.w_ih = mut(self.w_ih)
        self.b_h = mut(self.b_h)
        self.w_ho = mut(self.w_ho)
        self.b_o = mut(self.b_o)
