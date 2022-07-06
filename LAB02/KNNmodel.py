import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from LAB02 import imageProcessing


def KNN(X,Y):
    # initialisation du model KNN
    neigh = KNeighborsClassifier(n_neighbors=3)
    # convertis un tableau en tableau numpy
    numX = np.array(X)
    nsamples, nx, ny = numX.shape
    fx = numX.reshape((nsamples,nx*ny))
    neigh.fit(fx, Y)
    #prediction 
    print(neigh.predict(X[1]))


def main():
    #dataset
    X = imageProcessing.formatFolderPic("EnsembleB")
    Y = np.identity(8)

    KNN(X,Y)




if __name__ == "__main__":
    main()