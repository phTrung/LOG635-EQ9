from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from LAB02 import imageProcessing
import numpy as np
from sklearn import metrics


def SVM(X,Y):

    #Fait la séparation des données pour avoir les données X et Y de test et d'entrainement
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.2, random_state=59)

    #Création du classificateur
    clf = SVC(kernel='linear')
    clf.fit(Xtrain, Ytrain)

    #La prédiction
    Ypred = clf.predict(Xtest)

    return Xtrain, Xtest, Ytrain, Ytest, Ypred


def main():


    folder = "EnsembleB"
    #dataset
    X = imageProcessing.formatFolderPic(folder)
    Y = []

    #Creation de notre matrice ayant le même nombre de données que le nombre d'image dans l'ensemble B
    for i, direct in enumerate(folder):
        Y.append(i)

    Xtrain, Xtest, Ytrain, Ytest, Ypred = SVM(X,Y)

    #Génération des résultats grâce au données de SVM
    print("Accuracy:", metrics.accuracy_score(Ytest, Ypred))
    print("Precision:", metrics.precision_score(Ytest, Ypred))
    print("Recall:", metrics.recall_score(Ytest, Ypred))
    print("F-Mesure:", metrics.f1_score(Ytest,Ypred))


if __name__ == "__main__":
    main()