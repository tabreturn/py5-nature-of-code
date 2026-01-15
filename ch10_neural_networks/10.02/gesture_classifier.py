# https://natureofcode.com/neural-networks/#putting-the-network-in-neural-network

# ml5-style neural network functionality implemented with scikit-learn.
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

# Step 1: data
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

X = np.array([[d['x'], d['y']] for d in DATA], dtype=np.float32)
y = np.array([d['label'] for d in DATA])


# Step 2-3: model + scaler
scaler = StandardScaler()
mlp = MLPClassifier(
    hidden_layer_sizes=(8, 8),
    activation='tanh',
    solver='adam',
    max_iter=1,        # one epoch per fit()
    warm_start=True,
    random_state=0,
)


# Status + interaction
status = "training"
trained = False

start = None
end = None


# Training control
EPOCHS = 200
epoch_now = 0
progress = 0.0
last_loss = None

Xs = None
monospace = None


def setup():
    global Xs, monospace
    size(640, 240)
    monospace = create_font('DejaVu Sans Mono', 32)

    # Step 5: normalize data
    scaler.fit(X)
    Xs = scaler.transform(X)


def draw():
    global status, trained, epoch_now, progress, last_loss

    # Step 6: train (no threads): one epoch per frame
    if not trained:
        if epoch_now < EPOCHS:
            mlp.fit(Xs, y)  # one epoch
            epoch_now += 1
            progress = epoch_now / EPOCHS
            last_loss = float(mlp.loss_)
        else:
            trained = True
            status = "ready"

    # Step 7: render
    background(255)

    text_align(CENTER, CENTER)
    fill(0)
    text_size(64)
    text(status, width / 2, height / 2)

    if start is not None and end is not None:
        stroke(0)
        stroke_weight(8)
        line(start[0], start[1], end[0], end[1])

    # Display some info (Nature of Code style)
    no_stroke()
    fill(0)
    text_font(monospace)
    text_size(11)
    text_align(LEFT, TOP)  # <-- important: reset after CENTER,CENTER

    cycles_left = max(0, EPOCHS - epoch_now)
    if last_loss is None:
        hud = (
            f'Epoch #: {epoch_now}\n'
            f'Cycles left: {cycles_left}\n'
            f'Loss: -'
        )
    else:
        hud = (
            f'Epoch #: {epoch_now}\n'
            f'Cycles left: {cycles_left}\n'
            f'Loss: {last_loss:.6f}'
        )

    text(hud, 10, 20)
    text('(C) pause\n(Z) advance frame\n(X) run continuous\n(Q) quit', 10, 187)



def mouse_pressed():
    global start, end
    start = (mouse_x, mouse_y)
    end = None


def mouse_dragged():
    global end
    end = (mouse_x, mouse_y)


def mouse_released():
    global status, end

    if not trained or start is None:
        return

    if end is None:
        end = (mouse_x, mouse_y)

    # Step 8: classify direction
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy

    n = np.hypot(vx, vy)
    if n == 0:
        return

    direction = np.array([[vx / n, vy / n]], dtype=np.float32)
    direction_s = scaler.transform(direction)
    status = str(mlp.predict(direction_s)[0])


def key_pressed():
    if key == 'c':
        no_loop()
    if key == 'z':
        redraw()
    if key == 'x':
        loop()
    if key == 'q':
        exit_sketch()
