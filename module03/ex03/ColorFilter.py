import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter:

    def __init__(self):
        return

    def invert(self, array: np.ndarray):
        ret = np.ndarray(array.shape, dtype=array.dtype)
        ret = -array
        return ret

    def to_blue(self, array: np.ndarray):
        ret = np.zeros(array.shape, dtype=array.dtype)
        ln = len(array.shape)
        for i in range(0, len(array)):
            for j in range(0, len(array[0])):
                ret[i][j][2] = array[i][j][2]
                for k in range(3, ln):
                    ret[i][j][k] = array[i][j][k]
        return ret

    def to_green(self, array: np.ndarray):
        ret = np.ndarray(array.shape, dtype=array.dtype)
        ret = array * [0, 1, 0]
        return ret

    def to_red(self, array: np.ndarray):
        b = self.to_blue(array)
        g = self.to_green(array)
        ret = np.ndarray(array.shape, dtype=array.dtype)
        ret = array - (b + g)
        return ret

    # def to_celluloid(self, array: np.array):
    #     ret = np.ndarray(array.shape, dtype=array.dtype)
    #     div = 256 if type(ret[0][0][0]) == int else 1
    #     for i in range(len(array)):
    #         for j in range(len(array[0])):
    #             r = ret[i][j][0] / div
    #             g = ret[i][j][1] / div
    #             b = ret[i][j][2] / div
    #             luminence = 0.2126 * r + 0.7152 * g + 0.0722 * b
    #             if

    #     return ret

imp = ImageProcessor()
img = imp.load('musk.jpg', format='jpg')
# print(type(img.dtype))
imp.display(img)
cf = ColorFilter()
inv = cf.invert(img)
imp.display(inv)
blue = cf.to_blue(img)
imp.display(blue)
green = cf.to_green(img)
imp.display(green)
red = cf.to_red(img)
imp.display(red)
# cel = cf.to_celluloid(img)
# imp.display(cel)