# https://natureofcode.com/neural-networks/#putting-the-network-in-neural-network

# ml5-style neural network functionality implemented with scikit-learn.
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
  'max_iter': 25 * 100,         # Set the number of epochs for training.
  'verbose': True,              # The Shell will serve as the 'Visor'
  'hidden_layer_sizes': (16,),  # Approximate ml5 defaults
  # NOTE: scikit-learn infers input/output dimensionality from the data.
}

start = None
end = None


def setup():
    global monospace, classifier, scaler, status
    size(640, 240)
    monospace = create_font('DejaVu Sans Mono', 32)
    text_font(monospace)

    classifier = MLPClassifier(**OPTIONS)
    scaler = StandardScaler()

    # An array of two numbers for the inputs.
    inputs = [[item['x'], item['y']] for item in DATA]
    inputs = np.array(inputs)
    # A single string label for the output.
    outputs = [item['label'] for item in DATA]
    outputs = np.array(outputs)

    # Normalize the data.
    inputs = scaler.fit_transform(inputs)

    # Add the training data to the classifier.
    print(status := 'training')
    classifier.fit(inputs, outputs)  # fit() method initiates training process.
    print(status := 'ready')


def draw():
    background(255)

    text_align(CENTER, CENTER)
    fill(0)
    text_size(64)
    text(status, width / 2, height / 2 - 5)

    if start is not None and end is not None:
        stroke(0)
        stroke_weight(8)
        line(start.x, start.y, end.x, end.y)

    # Display some info.
    text_align(LEFT); text_font(monospace); text_size(11)
    text('\n'.join(
      f'dense_{i}  [batch,{W.shape[1]:>2}]  {W.size+b.size}'
      for i, (W, b) in enumerate(zip(classifier.coefs_, classifier.intercepts_), 1)
    ), 10, 20)
    text('Use the Shell to observe training performance', 10, 226)


def mouse_pressed():
    global start, end
    start = Py5Vector2D(mouse_x, mouse_y)
    end = None


def mouse_dragged():
    global end
    end = Py5Vector2D(mouse_x, mouse_y)


def mouse_released():
    global status
    v = (end - start).normalize()
    inputs = scaler.transform([[v.x, v.y]])
    status = str(classifier.predict(inputs)[0])
