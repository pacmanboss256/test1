import numpy
import typing

def data_gen(n: int) -> typing.Any:
	'''gives a random array of n random numbers between 0 and 1'''
	return numpy.random.random(size=n)