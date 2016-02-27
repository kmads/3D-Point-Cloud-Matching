__author__ = 'Holliday'
import time, csv, copy
from pcr_minDist import minDist

def readData(filename):
    start = time.clock()
    csvfile = open(filename, 'rb')
    dat = csv.reader(csvfile, delimiter=' ')
    pointCloud = []
    for i, row in enumerate(dat):
        pointCloud.append([row[0], row[1], row[2]])

    print time.clock() - start
    return pointCloud

if __name__ == '__main__':
    threshold = 100
    cloud1 = readData("pointcloud1.fuse")
    cloud2 = readData("pointcloud2.fuse")
    yk = minDist(cloud1, cloud2)
    # pk = copy.copy(cloud1)
    # qk = [1, 0, 0, ]
    #
    # # get the error of the first two iterations to use in the while loop condition
    # yk = minDist(pk, cloud2)
    # qk, dk1 = computeRegistration(cloud1, yk)
    # pk = applyRegistration(qk, cloud1)
    #
    # yk = minDist(pk, cloud2)
    # qk, dk2 = computeRegistration(cloud1, yk)
    # pk = applyRegistration(qk, cloud1)
    #
    #
    # while dk1 - dk2 > threshold:
    #     dk1 = dk2
    #     yk = minDist(pk, cloud2)
    #     qk, dk2 = computeRegistration(cloud1, yk)
    #     pk = applyRegistration(qk, cloud1)
    #
    # print qk