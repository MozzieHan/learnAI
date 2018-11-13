import numpy as np


def sigmoid(Z):
    A = 1.0/(1.0 + np.exp(-Z))
    assert(A.shape == Z.shape)
    return A


def sigmoid_backward(dA, Z):
    s = sigmoid(Z)
    dZ = dA * s * (1 - s)
    assert(dZ.shape==Z.shape)
    return dZ


def relu(Z):
    A = np.maximum(Z, 0)
    assert(A.shape == Z.shape)
    return A


def relu_backward(dA, Z):
    dZ = np.array(dA, copy=True)
    dZ[Z < 0] = 0
    assert(dZ.shape==Z.shape)
    return dZ
