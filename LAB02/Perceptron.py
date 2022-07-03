import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import pickle

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

class Perceptron:
    """Perceptron classifier."""

    def __init__(self, eta=0.1, n_iters=10):
        self.eta = eta
        self.n_iters = n_iters

    def train(self, X, y):
        """Function to train the neuron, which modifies the weights (w) based on the input values
        and expected results.
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iters):
            errors = 0
            for xi, target in zip(X, y):
                error = target - self.activation(xi)
                update = self.eta * error
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def activation(self, X):
        """Return class using Heaviside step function
        f(z) = 1 if z >= theta; 0 otherwise.
        """
        f = np.where(self.predict(X) >= 0.9, 1, 0)

        return f

    def predict(self, X):
        """Summation function."""
        # z = w · x + theta
        z = np.dot(X, self.w_[1:]) + self.w_[0]
        return z