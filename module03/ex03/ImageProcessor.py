import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


class ImageProcessor:
    path = None

    def __init__(self):
        return

    def load(self, path):
        self.path = path
        image = Image.open(path)
        width, height = image.size
        print('Loading images of dimensions %d x %d' % (width, height))
        var = np.array(image)
        return var

    def display(self, arr):
        plt.imshow(arr)
        plt.show()
