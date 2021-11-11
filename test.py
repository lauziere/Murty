
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial import distance
import os
import time

from getkBestNoRankHung import *
from InsertInfStrike import *
from parseClueOutput import *
from reconstructInitialPartition import *

if __name__ == '__main__':
	
	C = np.random.randn(100,100) + 12
	K = 50

	st = time.time()

	solutions, costs = getkBestNoRankHung(C,K)
	cols = solutions.argmax(axis=-1)

	rt = time.time() - st

	print('Finished in ', np.round(rt, 2), 'seconds.')
	print(costs)
