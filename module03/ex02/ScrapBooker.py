import numpy as np
from ImageProcessor import ImageProcessor


class ScrapBooker:
    vertc = 0
    horiz = 1

    def __init__(self):
        return

    def crop(self, array: np.ndarray, dimensions, position=(0, 0)):
        dim = dimensions
        pos = position
        if (dim[0] >= array.shape[0] or dim[1] >= array.shape[1]
           or pos[0] >= array.shape[0] or pos[1] >= array.shape[1]):
            return array
        croped = array[pos[0]:pos[0] + dim[0], pos[1]:pos[1] + dim[1]]
        return np.array(croped)

    def thin(self, array: np.ndarray, n, axis):
        if axis == self.horiz:
            return array[::n, ]
        return array[::, ::n]

    def juxtapose(self, array: np.ndarray, n, axis):
        return np.concatenate([array for _ in range(0, n)], axis=axis)

    def mosaic(self, array, dimensions):
        dim = dimensions
        return self.juxtapose(self.juxtapose(array, dim[0], 0), dim[1], 1)


imp = ImageProcessor()
img = imp.load('img.png')
sc = ScrapBooker()
imp.display(img)
croped = sc.crop(img, (300, 400), position=(300, 400))
imp.display(croped)
thin_x = sc.thin(img, 2, 0)
thin_y = sc.thin(img, 2, 1)
imp.display(thin_x)
imp.display(thin_y)
jp = sc.juxtapose(img, 5, 1)
imp.display(jp)
ms = sc.mosaic(img, (5, 5))
imp.display(ms)
