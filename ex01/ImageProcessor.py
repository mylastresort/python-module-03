import matplotlib.pyplot as plt

class ImageProcessor:
    def load(self, path):
        return plt.imread(path)
    def display(self, array):
        plt.imshow(array)