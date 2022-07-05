import os

from pathlib import Path

import matplotlib.pyplot as plt

import cv2

import numpy as np
import imutils
import random

import pickle

import ImageClassifier

from tabulate import tabulate

from squares import find_squares

WIDTH = 100

HEIGHT = 100


def formatFolderPic(folder):
    x = []
    for path in os.listdir(folder):
        picPath = str(folder) + "/" + str(path)
        x.append(formatPic(picPath))

    print(x)
    return x


def formatPic(path):
    image = cv2.imread(path)
    bitwise = cv2.bitwise_not(image)
    resized = cv2.resize(bitwise, (WIDTH, HEIGHT))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]

    imagearray = np.array(thresh)
    #cv2.imshow('image', imagearray)
    #cv2.waitKey(0)
    imagearray[imagearray == 255] = 1
    return imagearray.reshape(1, 10000)


def main():
    formatFolderPic("EnsembleB")


if __name__ == "__main__":
    main()
