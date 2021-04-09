from random import randint
import numpy as np


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
			random_index = randint(0, len(X))
			while random_index in indexes:
				random_index = randint(0, len(X))
			indexes.append(random_index)
			self.centroids.append(X[random_index])
		nitr = 0
		self.centroids = np.array(self.centroids)
		oldcen = self.centroids + 1
		while nitr < self.max_iter and np.all(oldcen != )


	def predict(self, X):
		"""Predict from wich cluster each datapoint belongs to.
		Args:X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns: the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises: This function should not raise any Exception."""
		belongs = np.full((len(X)), 0)
		for i, entry in enumerate(X):
			belongs[i] = self.centroids[self.closest(entry)]
		return belongs

obj = KmeansClustering()
print(obj.distance([0,0], [3,4]))