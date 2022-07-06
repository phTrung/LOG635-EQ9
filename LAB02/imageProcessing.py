import os
from pathlib import Path
import matplotlib.pyplot as plt
import cv2
import numpy as np
import imutils

WIDTH = 100

HEIGHT = 100


def formatFolderPic(folder):
    x = []
    #itération sur les images du fichier de l'ensemble B
    for path in os.listdir(folder):
        picPath = str(folder) + "/" + str(path)
        x.append(formatPic(picPath))

    print(x)
    return x

#methode pour le prétraitement des images
def formatPic(path):
    #cherche l'image
    image = cv2.imread(path)
    #inverse la valeur des pixels
    bitwise = cv2.bitwise_not(image)
    #redimentionne l'image en 100 par 100
    resized = cv2.resize(bitwise, (WIDTH, HEIGHT))
    #convertie l'image en gradient de gris
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    #L’opération de noyau gaussien est utilisée pour flouter un peu l’image.
    # Le flou gaussien est très efficace pour supprimer le bruit gaussien d'une image.
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #Extremise la valeur des pixels pour avoir que du noir ou bland (0 ou 255)
    thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]

    #convertie l'image en array numpy
    imagearray = np.array(thresh)
    #change les pixels de l'image pour avoir que des valeurs binaires
    imagearray[imagearray == 255] = 1
    #applatie la matrice pour avoir un vecteur
    return imagearray.reshape(1, 10000)


def main():
    formatFolderPic("EnsembleB")


if __name__ == "__main__":
    main()
