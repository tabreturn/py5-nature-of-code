# PY5 IMPORTED MODE CODE


class LSystem:
    """Construct an L-system with a starting sentence and a ruleset."""

    def __init__(self, axiom: str, rules: dict[str, str]) -> None:
        self.sentence = axiom  # The sentence (a String).
        self.rules = rules     # The ruleset (a dictionary of Rule objects).

    def generate(self) -> None:
        next_gen = ''.join(
          # Replace c with itself unless it matches one of our rules.
          self.rules.get(c, c)  # Give me rules[c] if it exists, otherwise c.
          for c in self.sentence
        )

        self.sentence = next_gen  # Replace sentence.
