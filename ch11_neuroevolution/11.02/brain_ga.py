# ml5.js-style neural network functionality implemented with bespoke class.

from __future__ import annotations
from py5 import np

_rng = np.random.default_rng()


class Brain:
    """Vectorized NumPy brain with GA helpers (drop-in-ish)."""

    def __init__(self, inputs: int, outputs: int, hidden: int = 8) -> None:
        self.n_in, self.n_h, self.n_out = inputs, hidden, outputs
        self.w_ih = _rng.uniform(-1.0, 1.0, (hidden, inputs))
        self.b_h  = _rng.uniform(-1.0, 1.0, (hidden,))
        self.w_ho = _rng.uniform(-1.0, 1.0, (outputs, hidden))
        self.b_o  = _rng.uniform(-1.0, 1.0, (outputs,))

    def copy(self) -> 'Brain':
        b = Brain(self.n_in, self.n_h, self.n_out)
        b.w_ih, b.b_h, b.w_ho, b.b_o = (
          self.w_ih.copy(), self.b_h.copy(),
          self.w_ho.copy(), self.b_o.copy(),
        )
        return b

    def forward(self, inputs: list[float]) -> list[float]:
        x = np.asarray(inputs, dtype=float)
        h = np.tanh(self.w_ih @ x + self.b_h)
        return (self.w_ho @ h + self.b_o).tolist()

    # Prediction methods.

    def predict_binary(self, inputs: list[float], threshold: float = 0.5) -> bool:
        z = self.forward(inputs)[0]
        p = 1.0 / (1.0 + np.exp(-z))
        return p > threshold

    def predict_flap(self, inputs: list[float]) -> bool:
        return (
          self.predict_binary(inputs)
          if self.n_out == 1
          else self.predict_class(inputs) == 0
        )

    def predict_continuous_01(self, inputs: list[float]) -> list[float]:
        raw = np.asarray(self.forward(inputs), dtype=float)
        return ((np.tanh(raw) + 1.0) * 0.5).tolist()

    def predict_probs(self, inputs: list[float]) -> list[float]:
        raw = np.asarray(self.forward(inputs), dtype=float)
        if self.n_out == 1:
            return [float(1.0 / (1.0 + np.exp(-raw[0])))]
        raw = raw - np.max(raw)
        e = np.exp(raw)
        return (e / np.sum(e)).tolist()

    def predict_class(self, inputs: list[float]) -> int:
        return int(np.argmax(self.forward(inputs)))

    # Crossover and mutation.

    @staticmethod
    def crossover(a: 'Brain', b: 'Brain') -> 'Brain':
        c = Brain(a.n_in, a.n_h, a.n_out)
        c.w_ih = np.where(_rng.random(a.w_ih.shape) < 0.5, a.w_ih, b.w_ih)
        c.b_h  = np.where(_rng.random(a.b_h.shape)  < 0.5, a.b_h,  b.b_h)
        c.w_ho = np.where(_rng.random(a.w_ho.shape) < 0.5, a.w_ho, b.w_ho)
        c.b_o  = np.where(_rng.random(a.b_o.shape)  < 0.5, a.b_o,  b.b_o)
        return c

    def mutate(self, rate: float = 0.01, sigma: float = 0.5) -> None:
        def mut(arr: np.ndarray) -> np.ndarray:
            m = _rng.random(arr.shape) < rate
            return arr + m * _rng.normal(0.0, sigma, arr.shape)

        self.w_ih = mut(self.w_ih)
        self.b_h  = mut(self.b_h)
        self.w_ho = mut(self.w_ho)
        self.b_o  = mut(self.b_o)