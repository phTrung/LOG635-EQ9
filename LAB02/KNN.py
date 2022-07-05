import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def run(X,Y):
    neigh = KNeighborsClassifier(n_neighbors=3)
    numX = np.array(X)
    nsamples, nx, ny = numX.shape
    fx = numX.reshape((nsamples,nx*ny))
    neigh.fit(fx, Y)
    print(neigh.predict(X[1]))