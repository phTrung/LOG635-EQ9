import numpy as np
import RNmodel
import imageProcessing
import pickle

def main():
    #dataset
    X = imageProcessing.formatFolderPic("LAB02/EnsembleB")
    print(len(X))
    # labels, matrice identité
    Y = np.identity(8)

    #Sauvegarde de la base de données en pickle.
    with open("XPickle.pickle", 'wb') as f:
        pickle.dump(X,f)

    with open("YPickle.pickle", 'wb') as f:
        pickle.dump(Y,f)

    #génération des poids au hazard
    w1 = RNmodel.random_weights(10000, 2000)
    w2 = RNmodel.random_weights(2000, 8)
    print(w1, "\n\n", w2)

    #appel à l'entrainement
    accuracy, loss, w1, w2 = RNmodel.train(X, Y, w1, w2, 0.01, 10)
    RNmodel.predict(X[1], w1, w2)
    

if __name__ == "__main__":
    main()
