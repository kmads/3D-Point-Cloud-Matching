__author__ = 'Holliday'
import time, csv, copy
from old_minDist import minDist
from registration import registration, R as createR
from getDK import getDk
import numpy as np
start = time.clock()


def readData(filename):
    csvfile = open(filename, 'rb')
    dat = csv.reader(csvfile, delimiter=' ')
    pointCloud = []
    # For now read in the first 1000 points of each point cloud
    j = 0
    for i, row in enumerate(dat):
        pointCloud.append([float(row[0]), float(row[1]), float(row[2])])
        j += 1
        if j == 1000:
            break

    print time.clock() - start
    return np.array(pointCloud)

if __name__ == '__main__':
    threshold = 100
    cloud1 = readData("pointcloud1.fuse")
    cloud2 = readData("pointcloud2.fuse")
    pk = copy.copy(cloud1)

    # get the error of the first two iterations to use in the while loop condition
    yk = minDist(pk, cloud2)
    qr, qt = registration(cloud1, yk)
    dk1 = getDk(qr, qt, cloud1, yk)
    # pk = np.subtract(np.dot(cloud1,createR(qr.transpose())), qt)
    pk = np.dot(np.subtract(cloud1, qt), createR(qr.transpose()))

    yk = minDist(pk, cloud2)
    print yk[0]
    qr, qt = registration(cloud1, yk)
    dk2 = getDk(qr, qt, cloud1, yk)
    # pk = np.subtract(np.dot(cloud1,createR(qr.transpose())), qt)
    pk = np.dot(np.subtract(cloud1, qt), createR(qr.transpose()))

    print "DK: ", dk1, dk2

    while dk1 - dk2 > threshold:
        dk1 = dk2
        yk = minDist(pk, cloud2)
        qr, qt = registration(cloud1, yk)
        dk2 = getDk(qr, qt, cloud1, yk)
        # pk = np.subtract(np.dot(cloud1,createR(qr.transpose())), qt)
        pk = np.dot(np.subtract(cloud1, qt), createR(qr.transpose()))
    # concat qr and qt together into q

    print np.concatenate([qr, qt],1)
    #print np.testing.assert_allclose(pk, cloud2, rtol=.0001, atol=0)
    print time.clock() - start
