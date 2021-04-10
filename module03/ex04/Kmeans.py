from random import randint
import numpy as np
from csvreader import CsvReader
from tabulate import tabulate
from time import sleep
import matplotlib.pyplot as plt


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def distance(self, a, b):
        return sum((c - d) ** 2 for c, d in zip(a, b)) ** 0.5

    def closest(self, a):
        lst = []
        for b in self.centroids:
            lst.append(self.distance(a, b))
        return lst.index(min(lst))

    def fit(self, X):
        """Run the K-means clustering algorithm.For the location of the initial
        centroids, random pick ncentroids from the dataset.
        Args:X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns: None.
        Raises: This function should not raise any Exception."""
        indexes = []
        for _ in range(self.ncentroid):
            random_index = randint(0, len(X) - 1)
            while random_index in indexes:
                random_index = randint(0, len(X) - 1)
            indexes.append(random_index)
            self.centroids.append(X[random_index])
        self.centroids = np.array(self.centroids)
        # print(self.centroids)
        oldcen = self.centroids + 1
        nitr = 0
        print('------------')
        print('initial:')
        print(self.centroids)
        print('------------')
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        while nitr < self.max_iter and not np.all(oldcen == self.centroids):
            oldcen = self.centroids.copy()
            belong = self.predict(X)
            for i in range(len(belong)):
                self.centroids[i] = (np.sum(np.array(belong[i]), axis=0)
                                    / len(belong[i]))
            fig = plt.figure(figsize=(4,4))
            ax = fig.add_subplot(111, projection='3d')
            for i in range(len(X)):
                ax.scatter(X[i][0],X[i][1],X[i][2])
            for i in range(len(self.centroids)):
                ax.scatter(self.centroids[i][0], self.centroids[i][1], self.centroids[i][2], c=colors[i], marker='x')
                for j in range(len(belong[i])):
                    ax.scatter(belong[i][j][0], belong[i][j][1], belong[i][j][2], c=colors[i])
            plt.show()
            nitr += 1

        print('nitr:', nitr)
        print('------------')
        print('final:')
        print(self.centroids)
        print('------------')

    def predict(self, X):
        """Predict from wich cluster each datapoint belongs to.
        Args:X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns: the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises: This function should not raise any Exception."""
        belongs = [[] for _ in range(self.ncentroid)]
        for entry in X:
            belongs[self.closest(entry)].append(entry) 
        return belongs

km = KmeansClustering(ncentroid=4)
with CsvReader('solar_system_census.csv', header=True) as citizens:
    if citizens is None:
        print('file is corrupt')
    else:
        data = citizens.get_data()
        header = citizens.get_header()
        # citizens.tabulate()
        npc = np.array(citizens.data).astype('longdouble')
        npc = npc[:, 1:]
        # print(npc)
        km.fit(npc)
        """
        Belt: max height, ? weight, min bone-den | bH, bW, bB
        Mars: mH > eH   , ? weight, ?   bone-den | mH, mW, mB
        Erth: eH < mH   , eW > vW , ?   bone-den | eH, eW, eB
        Vnus: ?   height, vW < eW , ?   bone-den | vH, vW, vB
        [196.31882434  96.72908505   0.78466393] ? Belt
        [194.85778543  71.9904936    0.78904601] ? Mars
        [182.30688779  86.2436454    0.86820468] ? Earth
        [170.96978009  74.22752665   0.95362633] ? Venus
        """