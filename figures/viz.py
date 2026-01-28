import matplotlib.pyplot as plt
import numpy as np
import os

PATH_FIG = 'figures'

# figures only pls


def makeFigure(data: np.ndarray, filename: str) -> None:

	'''Input nx2 numpy array, save figure to specified filename'''

	full_filename = os.path.join(PATH_FIG, filename)

	if not os.path.exists(PATH_FIG):
		os.mkdir(PATH_FIG)

	
	plt.figure(figsize=(6,6))
	plt.scatter(data[:, 0], data[:,1])
	plt.savefig(full_filename, bbox_inches='tight')
	plt.show()
	
	return None