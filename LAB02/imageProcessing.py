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
    # Resize, ignoring aspect ratio
    for path in os.listdir(folder):
        # print(folder)
        print(str(path))
        picPath = str(folder) + "/" + str(path)
        formatPic(picPath)

        # plt.imshow(thresh, cmap='gray')

        # cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cnts = imutils.grab_contours(cnts)


def formatPic(path):
    image = cv2.imread(path)
    # resized = cv2.resize(image, (WIDTH, HEIGHT))
    bitwise = cv2.bitwise_not(image)
    resized = cv2.resize(bitwise, (WIDTH, HEIGHT))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]

    # detect contour carre
    squares = find_squares(thresh)
    cv2.drawContours(resized, squares, -1, (0, 255, 0), 2)

    cropped_image = thresh
    if len(squares) != 0:
        # crop the grayscale image with the contours
        cropped_image = cropped_image[(squares[0].min(axis=1)).min():(squares[0].max(axis=1)).max(), (squares[0].min(axis=0)).min(): (squares[0].max(axis=0)).max()]
        # cv2.imshow('image1', cropped_image)
        # cv2.waitKey(0)
    cv2.imwrite("EnsembleA_H2022/Cercles/Cercle2" + "_resized/" + os.path.basename(path), cropped_image)

    imageArray = np.array(thresh)
    imageArray[imageArray == 255] = 1

    print("A")


def main():
    formatFolderPic("EnsembleA_H2022/Cercles/Cercle2")


if __name__ == "__main__":
    main()
