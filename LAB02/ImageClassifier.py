from PIL import Image
import numpy as np
import pickle

class ImageClassifier:

    #database pour classer l'image
    def __init__(self, databaseName):
        self.database = None
        self.databaseName = databaseName

    def __str__(self):
        if not self._database == None:
            return("ImageRegognizer with database of"
                   + str(len(self._database))
                   + " defferent Classes, each containing "
                   + str(len(self._database[0])) + " images.")

    '''prend un dossier dans lequel sont stocké les images
    et un nom d'une base de données qui sera créée contenant
    les représentations de ces images'''
    @staticmethod
    def createDatabase(imageFolder, databaseName):
        number_db = {}
        for i in range(10):
            number_db[i] = []
        for number in range(len(number_db.keys())):
            for index in range(16):
                image = Image.open(imageFolder + "/" + str(number) + "_" + str(index) + ".jpg")
                number_db[number].append(np.array(image).tolist())

        with open(databaseName + ".pkl", "wb") as db:
            pickle.dump(number_db,db)

    def openDatabase(self):
        with open(self._databaseName+".pkl", "rb") as db:
            self._database = pickle.load(db)

    '''Prend une image qu'il faut normaliser.'''
    @staticmethod
    def normalizeBinary(image):
        for column in image:
            for pixel in range(len(column)):
                total_color = 0
                for color in column[pixel]:
                    total_color += color
                if total_color/3 < 255/2:
                    column[pixel] = 0
                else:
                    column[pixel] = 1
        return image

    @staticmethod
    def normalizeNot(image):
        return image

    def normalizeDatabase(self, normFunction):
        for number in range(len(self._database.keys())):
            for image in self._database[number]:
                image = normFunction(image)

    def classifyImage(self, img, normFunction):
        test_image = Image.open(img)
        test_image = np.array(test_image).tolist()
        test_image = normFunction(test_image)