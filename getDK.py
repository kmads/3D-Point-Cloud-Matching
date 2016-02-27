import time, math

# call the getDk function to get value of dk with params qkR, qkT, P = point cloud 1 and y = closest points

def createR(qkR):
	q0 = qkR[0]
	q1 = qkR[1]
	q2 = qkR[2]
	q3 = qkR[3]

	R = np.random.randint(9, size = (3,3))

	R(0,0) = math.pow(q0, 2) + math.pow(q1, 2) + math.pow(q2, 2) - math.pow(q3, 2)
	R(0,1) = 2 * ((q1 * q2) - (q0 * q3))
	R(0,2) = 2 * ((q1 * q3) + (q0 * q2))
	R(1,0) = 2 * ((q1 * q2) + (q0 * q3))
	R(1,1) = math.pow(q0, 2) + math.pow(q2, 2) - math.pow(q1, 2) - math.pow(q3, 2)
	R(1,2) = 2 * ((q2 * q3) - (q0 * q1))
	R(2,0) = 2 * ((q1 * q3) - (q0 * q2))
	R(2,1) = 2 * ((q2 * q3) + (q0 * q1))
	R(2,2) = math.pow(q0, 2) + math.pow(q3, 2) - math.pow(q1, 2) - math.pow(q2, 2)
	
	return R

def eachDki(qkR, qkT, yik, Pi0):
	R = createR(qkR)
	RPi0 = #matrix multiply
	temp = np.subtract(yik, RPi0)
	n_i_sqrt = np.subtract(temp, qkT)

	n_i = math.pow(n_i_sqrt, 2)

	return n_i

def getDk(qkR, qkT, P, y): 
	d_k = None
	sumN = 0
	length = len(P)

	for i in range(0, length):
		yik = y[i]
		Pi0 = P[i]
		sumN += eachDki(qkR, qkT, yik Pi0)
	d_k = sumN / length

	return sumN
