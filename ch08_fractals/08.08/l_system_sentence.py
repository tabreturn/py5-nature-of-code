# https://natureofcode.com/fractals/#example-88-simple-l-system-sentence-generation

current = 'A'  # Start with an axiom.


def setup():
    size(640, 240)
    background(255)
    no_loop()

    monospace = create_font('../../DejaVuSansMono.ttf', 32)

    for i in range(9):
        # Render text to canvas.
        fill(0)
        text_font(monospace)
        text_size(16)
        text(f'{i}: {current}', 4, 20 + i * 16)

        generate()  # Generate the next sentence.


def generate() -> None:
    global current

    next_ = "".join(
      # Apply the production rules A → AB, B → A ...
      'AB' if c == 'A' else 'A' if c == 'B' else c
      for c in current  # ... for every character of the current sentence.
    )

    current = next_  # Save the next generation.
