import numpy as np
from ImageProcessor import ImageProcessor


class ColorFilter:

    def __init__(self):
        return

    def invert(self, array: np.ndarray):
        mx = 1 if type(array[0][0][0]) == float else 255
        array[:, :, 0:3] = mx - array[:, :, 0:3]
        return array

    def to_blue(self, array: np.ndarray):
        ret = np.zeros(array.shape, dtype=array.dtype)
        ret[:, :, 2] = array[:, :, 2]
        for i in range(3, len(array[0][0])):
            ret[:, :, i] = array[:, :, i]
        return ret

    def to_green(self, array: np.ndarray):
        array[:, :, 0] *= 0
        array[:, :, 2] *= 0
        return array

    def to_red(self, array: np.ndarray):
        red = self.to_blue(array)
        red = self.to_green(red)
        red[:, :, 0] = array[:, :, 0]
        return red

    def to_celluloid(self, array: np.ndarray):
        array[array[:, :, 0] <= 64, 0] = 0
        array[array[:, :, 1] <= 64, 1] = 0
        array[array[:, :, 2] <= 64, 2] = 0
        array[((array <= 128) & (array > 64))[:, :, 0], 0] = 64
        array[((array <= 128) & (array > 64))[:, :, 1], 1] = 64
        array[((array <= 128) & (array > 64))[:, :, 2], 2] = 64
        array[array[:, :, 0] > 128, 0] = 128
        array[array[:, :, 1] > 128, 1] = 128
        array[array[:, :, 2] > 128, 2] = 128
        return array

    def to_grayscale(self, array: np.ndarray, filter):
        if filter == 'm' or filter == 'mean':
            array[:, :, 0:3] = np.sum(array[:, :, 0:3] / 3, axis=2,
                                      keepdims=True).astype(array.dtype)
        else:
            array[:, :, 0:3] = np.sum([array[:, :, 0:1] * 0.299,
                                      array[:, :, 1:2] * 0.587,
                                      array[:, :, 2:3] * 0.114], axis=0)
        return array


cf = ColorFilter()
imp = ImageProcessor()
# img = imp.load('flowers.png')
# img = imp.load('dice.png')
img = imp.load('musk.jpg')
# img = imp.load('test.png')
imp.display(img)
inv = cf.invert(img.copy())
print('inverted')
imp.display(inv)
blue = cf.to_blue(img.copy())
print('blue')
imp.display(blue)
red = cf.to_red(img.copy())
print('red')
imp.display(red)
green = cf.to_green(img.copy())
print('green')
imp.display(green)
cel = cf.to_celluloid(img.copy())
print('cel')
imp.display(cel)
grm = cf.to_grayscale(img.copy(), 'm')
print('grey_m')
imp.display(grm)
grw = cf.to_grayscale(img.copy(), 'w')
print('grey_w')
imp.display(grw)
diff = grw[:, :, 0:3] - grm[:, :, 0:3]
print('diff')
imp.display(diff)
