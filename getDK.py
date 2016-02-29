import time, math, numpy as np
from registration import R as createR
# call the getDk function to get value of dk with params qkR, qkT, P = point cloud 1 and y = closest points

def eachDki(R, qkT, yik, Pi0):
	RPi0 = np.multiply(Pi0, R) #matrix multiply
	temp = np.subtract(yik, RPi0)
	n_i_sqrt = np.subtract(temp, qkT)
	n_i = math.pow(n_i_sqrt, 2)

	return n_i

def getDk(qk, P, y):
	sumN = 0
	length = len(P)
	qkR = qk[:4]
	qkT = qk[4:7]
	R = createR(qkR)
	for i in range(0, length):
		yik = y[i]
		Pi0 = P[i]
		sumN += eachDki(R, qkT, yik, Pi0)
	d_k = sumN / length

	return d_k
