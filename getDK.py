import time, math, numpy as np
from registration import R as createR
# call the getDk function to get value of dk with params qkR, qkT, P = point cloud 1 and y = closest points

def eachDki(R, qkT, yik, Pi0):
	RPi0 = np.mat(Pi0) * np.mat(R) #matrix multiply
	n_i_mag = np.linalg.norm(yik - RPi0 - qkT) # Find the magnitude/Euclidean norm
	n_i = n_i_mag**2
	return n_i

def getDk(qkR, qkT, P, y):
	start = time.clock()
	sumN = 0
	length = len(P)
	R = createR(qkR.transpose())
	for i in range(0, length):
		yik = y[i]
		Pi0 = P[i]
		sumN += eachDki(R, qkT, yik, Pi0)
	d_k = sumN / float(length)
	print time.clock() - start
	return d_k
