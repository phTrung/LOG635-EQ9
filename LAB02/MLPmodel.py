from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from LAB02 import imageProcessing
from sklearn import metrics


def MLP(X, y):
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.2, random_state=59)
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(Xtrain, Ytrain)
    Ypred = clf.predict(Xtest)

    return Xtrain, Xtest, Ytrain, Ytest, Ypred

def main():

    folder = "EnsembleB"
    #dataset
    X = imageProcessing.formatFolderPic(folder)
    Y = []

    for i, direct in enumerate(folder):
        Y.append(i)

    Xtrain, Xtest, Ytrain, Ytest, Ypred = MLP(X,Y)

    print("Accuracy:", metrics.accuracy_score(Ytest, Ypred))
    print("Precision:", metrics.precision_score(Ytest, Ypred))
    print("Recall:", metrics.recall_score(Ytest, Ypred))
    print("F-Mesure:", metrics.f1_score(Ytest,Ypred))


if __name__ == "__main__":
    main()
