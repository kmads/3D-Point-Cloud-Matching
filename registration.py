__author__ = 'Misha Kushnir'

from Quaternion import Quat
import numpy as np

## GENERATE QKR and QKT

def registration(P, X):
    # (qk, dk) = Q(P0, Yk). Cost: O(Np)

    up = centerOfMass(P) # "center of mass" of measured point set P
    ux = centerOfMass(X) # center of mass for X point set

    print "\nCenter of mass of P:"
    print up
    print "\nCenter of mass of X:"
    print ux

    # cross-covariance matrix
    sigmapx = crossCovariance(P, X, up, ux)
    print "\nCross covariance matrix:"
    print sigmapx

    # Aij = (sigmapx - sigmaTpx)ij
    A = sigmapx - sigmapx.transpose()
    print "\nAij:"
    print A

    # delta = [A23 A31 A12]T

    delta = np.array([[A[1,2], A[2,0], A[0,1]]]).transpose()
    print "\nDelta:"
    print delta

    I3 = np.identity(3)
    # tr() = trace of a matrix = sum of elements along main diagonal
    trace = sigmapx[0,0] + sigmapx[1,1] + sigmapx[2,2]

    # Q(sigmapx) = [ tr(sigmapx)                deltaT
    #                delta          sigmapx + sigmaTpx - tr(sigmapx)I3 ]
    Qsigmapx = np.zeros((4,4))
    Qsigmapx[0,0] = trace
    Qsigmapx[0,1:4] = delta.transpose()

    #there's definitely a better way to do this but I kept running into weird reshaping problems
    Qsigmapx[1,0] = delta[0]
    Qsigmapx[2,0] = delta[1]
    Qsigmapx[3,0] = delta[2]

    Qsigmapx[1:4,1:4] = sigmapx + sigmapx.transpose() - trace*I3

    print "\nQ(cross covariance matrix):"
    print Qsigmapx

    # qr = eigenvector corresponding to the max eigenvalue of Qsigmapx is the optimal rotation
    # w = eigenvalues, v = eigenvectors (see numpy.linalg.eig documentation)
    (w, v) = np.linalg.eig(Qsigmapx)

    print "\nEigenvalues:"
    print w
    maxEigenvalue = max(w)
    print "\nMax eigenvalue:"
    print maxEigenvalue
    maxIndex = w.tolist().index(maxEigenvalue)
    qr = np.array([v[maxIndex]]).transpose()

    print "\nTransposed eigenvector for max eigenvalue (optimal rotation vector qr):"
    print qr


    qt = ux - R(qr)*up # optimal translation vector

    print "\nqt (optimal translation vector):"
    print qt

    # final registration vector q = [qr|qt]t
    q = [qr.transpose(), qt.transpose()]
    return q

# q is a 4x1 array
def R(q):
    [q0, q1, q2, q3] = q

    R = np.zeros((3,3))
    R[0,0] = q0*q0 + q1*q1 - q2*q2 - q3*q3
    R[0,1] = 2*(q1*q2 - q0*q3)
    R[0,2] = 2*(q1*q3 + q0*q2)
    R[1,0] = 2*(q1*q2 + q0*q3)
    R[1,1] = q0*q0 + q2*q2 - q1*q1 - q3*q3
    R[1,2] = 2*(q2*q3 - q0*q1)
    R[2,0] = 2*(q1*q3 - q0*q2)
    R[2,1] = 2*(q2*q3 + q0*q1)
    R[2,2] = q0*q0 + q3*q3 - q1*q1 -q2*q2

    print "\nR:"
    print R

    return R

def crossCovariance(P, X, up, ux):

    Np = len(P)

    sum = np.zeros((3,3))
    for i in range(0, Np):
        Pi = np.array(P[i])
        Xi = np.array(X[i])

        x = Pi * Xi.transpose()
        sum += x

    return sum / float(Np) - up * ux.transpose()


def centerOfMass(X):

    Nx = len(X)

    sum = np.zeros(3)
    for i in range(0, len(X)):
        Xi = np.array([[X[i][0], X[i][1], X[i][2]]])
        sum = sum + Xi

    return sum / float(Nx)



if __name__=="__main__":
    P = [[0.0, 0.4, 1.0], [1.3, 6.4, 2.3]]
    X = [[3.2, 1.3, 0.4], [2.2, 2.2, 1.9]]

    reg = registration(P, X)