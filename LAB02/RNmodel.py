# activation function
import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward_propagation(x, w1, w2):
    # couche cache
    z1 = x.dot(w1)
    a1 = sigmoid(z1)

    # couche de sortie
    z2 = a1.dot(w2)
    a2 = sigmoid(z2)
    return a2


# generer les weights aléatoirement
def random_weights(x, y):
    l = []
    for i in range(x * y):
        l.append(np.random.randn())
    return np.array(l).reshape(x, y)


# Fonction de coût se basant sur Mean squared error (MSE)
def loss(out, Y):
    s = (np.square(out - Y))
    s = np.sum(s) / 2 * len(Y)
    return s


# Algorithme de rétropropagation pour les erreurs
def back_propagation(x, y, w1, w2, learning_rate):
    # couche cache
    z1 = x.dot(w1)
    a1 = sigmoid(z1)

    # couche de sortie
    z2 = a1.dot(w2)
    a2 = sigmoid(z2)

    d2 = (a2 - y)
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(),
                     (np.multiply(a1, 1 - a1)))

    # Gradient descent pour mettre à jour les weights
    d_W2 = a1.transpose().dot(d2)
    d_W1 = x.transpose().dot(d1)
    w1 = w1 - (learning_rate * d_W1)
    w2 = w2 - (learning_rate * d_W2)

    return w1, w2


def train(x, Y, w1, w2, learning_rate=0.01, num_iterations=10):
    acc = []
    losss = []
    for j in range(num_iterations):
        l = []
        for i in range(len(x)):
            out = forward_propagation(x[i], w1, w2)
            l.append((loss(out, Y[i])))
            w1, w2 = back_propagation(x[i], Y[i], w1, w2, learning_rate)
        print("epochs:", j + 1, "======== acc:", (1 - (sum(l) / len(x))) * 100)
        acc.append((1 - (sum(l) / len(x))) * 100)
        losss.append(sum(l) / len(x))
    return acc, losss, w1, w2


def predict(x, w1, w2):
    output = forward_propagation(x, w1, w2)
    maxm = 0
    k = 0
    for i in range(len(output[0])):
        if maxm < output[0][i]:
            maxm = output[0][i]
            k = i
    if k == 0:
        print("Image is Cercle2.")
    elif k == 1:
        print("Image is Cercle4.")
    elif k == 2:
        print("Image is Cercle4.")
    elif k == 3:
        print("Image is Diamant2.")
    elif k == 4:
        print("Image is Diamant4.")
    elif k == 5:
        print("Image is Hexagone2.")
    elif k == 6:
        print("Image is Hexagone4.")
    elif k == 7:
        print("Image is Triangle2.")
    else:
        print("Image is Triangle4.")

    plt.imshow(x.reshape(100, 100))
    plt.show()
