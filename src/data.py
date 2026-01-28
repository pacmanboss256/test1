import numpy as np
import os
import typing
from numpy.typing import NDArray

PATH_DATA = 'data'

# this file works with data please do not bitcoin mine


def makeData(n: int=100, low: int = 0, high: int = 25) -> NDArray:
	'''return n x 2 array of random ints between two specified values'''
	return np.random.randint(low=low,high=high+1,size=(n,2))


def saveData(data: NDArray, filename: str) -> None:
	'''save np array to default output folder, ensure folder exists'''

	full_filename = os.path.join(PATH_DATA, filename)

	# check output exists

	if not os.path.exists(PATH_DATA):
		os.mkdir(PATH_DATA)
	
	if type(data) != NDArray:
		raise TypeError(f'data should be a numpy array, found {type(data)} instead')
	
	# don't overwrite filename
	if os.path.exists(full_filename):
		raise FileExistsError(f'file {full_filename} already exists')
	
	# save as .npy
	np.save(full_filename, data)

	return None


def loadData(filename: str) -> NDArray:
	'''load data from .npy file'''
	return np.load(os.path.join(PATH_DATA, filename))