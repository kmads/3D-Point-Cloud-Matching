import time, math, numpy as np

def minDist(pc1, pc2):
	start = time.clock()

	minArray = []
	length = len(pc1)
	print("Length " + str(length))

	for i in range(0,length):
		min_pc2 = []
		min_dist = 100
		for j in range(0, length):
			dist = np.linalg.norm(np.subtract(pc2[j], pc1[i]))
			if dist < min_dist:
				min_dist = dist
				min_pc2 = pc2[j]
		minArray.append(min_pc2)

	end = time.clock()
	print("Finished in " + str(end-start) + "seconds")

	return np.array(minArray)

def distLLE(lat1, lon1, alt1, lat2, lon2, alt2):
  earth_rad = 6378137
  alt1 += earth_rad
  alt2 += earth_rad

  lat1r = math.radians(lat1)
  lon1r = math.radians(lon1)
  lat2r = math.radians(lat2)
  lon2r = math.radians(lon2)

  x1 = alt1 * math.cos(lat1r) * math.sin(lon1r)
  x2 = alt2 * math.cos(lat2r) * math.sin(lon2r)

  y1 = alt1 * math.sin(lat1r)
  y2 = alt2 * math.sin(lat2r)

  z1 = alt1 * math.cos(lat1r) * math.cos(lon1r)
  z2 = alt2 * math.cos(lat2r) * math.cos(lon2r)

  dist = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2) + math.pow((z2-z1), 2))
  return dist
