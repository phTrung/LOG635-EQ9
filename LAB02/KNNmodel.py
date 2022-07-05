import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from LAB02 import imageProcessing


def KNN(X,Y):
    neigh = KNeighborsClassifier(n_neighbors=3)
    numX = np.array(X)
    nsamples, nx, ny = numX.shape
    fx = numX.reshape((nsamples,nx*ny))
    neigh.fit(fx, Y)
    print(neigh.predict(X[1]))


def main():
    #dataset
    X = imageProcessing.formatFolderPic("EnsembleB")
    Y = np.identity(8)

    KNN(X,Y)




if __name__ == "__main__":
    main()