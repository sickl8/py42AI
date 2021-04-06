import matplotlib.pyplot as plt
from PIL import Image


class ImageProcessor:
    path = None

    def __init__(self):
        return

    def load(self, path):
        self.path = path
        image = Image.open(path)
        width, height = image.size
        print('Loading images of dimensions %d x %d' % (width, height))
        return plt.imread(path)

    def display(self, arr):
        plt.imshow(arr)


imp = ImageProcessor()
arr = imp.load('img.png')
print(arr)
imp.display(arr)
