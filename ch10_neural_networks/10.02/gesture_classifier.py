# https://natureofcode.com/neural-networks/#putting-the-network-in-neural-network

"""
NOTE: In this sketch, the model is trained before setup() runs.
Because of this, callbacks (see asynchronous operations) are not required.
"""

# ml5.js-style neural network functionality implemented with scikit-learn.
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

DATA = [
  {'x': 0.99, 'y': 0.02, 'label': 'right'},
  {'x': 0.76, 'y': -0.1, 'label': 'right'},
  {'x': -1.0, 'y': 0.12, 'label': 'left'},
  {'x': -0.9, 'y': -0.1, 'label': 'left'},
  {'x': 0.02, 'y': 0.98, 'label': 'down'},
  {'x': -0.2, 'y': 0.75, 'label': 'down'},
  {'x': 0.01, 'y': -0.9, 'label': 'up'},
  {'x': -0.1, 'y': -0.8, 'label': 'up'},
]

OPTIONS = {
  # NOTE: scikit-learn infers input/output dimensionality from the data.
  'max_iter': 25 * 100,         # Set the number of 'epochs' for training.
  'verbose': True,              # The Shell will serve as the 'Visor'.
  'hidden_layer_sizes': (16,),  # Approximate ml5.js 'best guess' configuration.
}
classifier = MLPClassifier(**OPTIONS)

# An array of two numbers for the inputs.
inputs = [[item['x'], item['y']] for item in DATA]
inputs = np.array(inputs)
# A single string label for the output.
outputs = [item['label'] for item in DATA]
outputs = np.array(outputs)

# Normalize the data.
scaler = StandardScaler()
inputs = scaler.fit_transform(inputs)

# Add the training data to the classifier.
print(status := 'training')  # When the sketch starts, show status of training.
classifier.fit(inputs, outputs)  # The fit() method initiates training process.
# No callback required for when training is complete, just display ready.
print(status := 'ready')

start, end = None, None


def setup():
    global monospace
    size(640, 240)
    monospace = create_font('DejaVu Sans Mono', 32)
    text_font(monospace)
    

def draw():
    background(255)

    text_align(CENTER, CENTER)
    fill(0)
    text_size(64)
    text(status, width / 2, height / 2)

    if start is not None and end is not None:
        stroke(0)
        stroke_weight(8)
        line(start.x, start.y, end.x, end.y)

    # Display some info.
    text_align(LEFT); text_font(monospace); text_size(11)
    text(f'{"Layer":<10} {"Shape":<10} Params\n' + '\n'.join(
      f'{(f"hidden_{i}" if i < len(classifier.coefs_) else "output"):<10} '
      f'{str(W.shape):<10} {W.size + b.size:}'
      for i, (W, b) in enumerate(zip(classifier.coefs_, classifier.intercepts_), 1)
    ),10, 20)
    text('* Use the Shell to observe training performance', 10, 226)


def mouse_pressed():
    # Store the start of a gesture when the mouse is pressed.
    global start
    start = Py5Vector2D(mouse_x, mouse_y)


def mouse_dragged():
    # Update the end of a gesture as the mouse is dragged.
    global end
    end = Py5Vector2D(mouse_x, mouse_y)


def mouse_released():
    """The gesture is complete when the mouse is released."""
    # Calculate and normalize a direction vector.
    direction = (end - start).normalize()
    # Convert to an input array and classify.
    inputs = scaler.transform([[direction.x, direction.y]])
    got_results(
      classifier.predict(inputs)[0],                # status
      probas = classifier.predict_proba(inputs)[0]  # confidences
    )


def got_results(label, probas) -> None:
    """Store resulting label in the status variable for showing in canvas."""
    global status
    status = str(label)

    # Log model predictions with confidence scores for each label.
    results = [
      {'label': l, 'confidence': float(p)}
      for l, p in zip(classifier.classes_, probas)
    ]
    print(*results, sep='\n', end='\n\n')