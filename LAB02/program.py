import numpy as np
import RNmodel
import KNNmodel
import imageProcessing


def main():
    #dataset
    X = imageProcessing.formatFolderPic("LAB02/EnsembleB")
    print(len(X))
    # labels
    Y = np.identity(8)

    w1 = RNmodel.random_weights(10000, 2000)
    w2 = RNmodel.random_weights(2000, 8)
    print(w1, "\n\n", w2)

    acc, loss, w1, w2 = RNmodel.train(X, Y, w1, w2, 0.01, 10)
    RNmodel.predict(X[1], w1, w2)
    KNN.run(X,Y)
    

if __name__ == "__main__":
    main()
