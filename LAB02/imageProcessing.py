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


WIDTH = 160

HEIGHT = 120



def detect_shape(contour):

    # initialize the shape name and approximate the contour

    shape = "unidentified"

    peri = cv2.arcLength(contour, True)

    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)


    # if the shape is a triangle, it will have 3 vertices

    if len(approx) == 3:

        shape = "triangle"


    # if the shape has 4 vertices, it is either a square or

    # a rectangle

    elif len(approx) == 4:

        # compute the bounding box of the contour and use the

        # bounding box to compute the aspect ratio

        (x, y, w, h) = cv2.boundingRect(approx)

        ar = w / float(h)


        # a square will have an aspect ratio that is approximately

        # equal to one, otherwise, the shape is a rectangle

        shape = "square" if ar >= 0.95 and ar <= 1.05 else "diamond"


    # if the shape is a pentagon, it will have 5 vertices

    elif len(approx) == 5:

        shape = "hexagon"


    # otherwise, we assume the shape is a circle

    else:

        shape = "circle"


    # return the name of the shape
    return shape



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
    imagearray[imagearray == 255] = 1
    imagearray = imagearray.flatten()
    return imagearray



def main():

    formatFolderPic("EnsembleB")



if __name__ == "__main__":
    main()

