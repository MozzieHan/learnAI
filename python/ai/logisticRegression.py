import numpy as np
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage

# %matplotlib inline

def sigmoid(z):
    s = 1.0/(1.0+np.exp(-z))
    return s

def initialize_with_zeros(dim):
    w = np.zeros((dim,1))
    b = 0
    assert(w.shape==(dim, 1))
    return w, b

def propagate(w, b, X, Y):
    m = X.shape[1]

    A = sigmoid(np.dot(w.T, X) + b)
    cost = -1/m * np.sum(
        (Y * np.log(A)) + (1-Y) * np.log(1 - Y)
    )
    
    dw = 1/m * np.dot(X, (A-Y).T)
    db = 1/m * np.sum(A - Y)

    assert(dw.shape == w.shape)
    assert(db.dtype == float)
    cost = np.squeeze(cost)
    assert(cost.shape == ())

    grads = {
        "dw": dw,
        "db": db,
    }

    return grads, cost

def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost=False):
    costs = []

    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)

        dw, db = grads["dw"], grads["db"]

        w = w - learning_rate * dw
        b = b - learning_rate * db
        if i % 100 == 0:
            costs.append(costs)
    params = {
        "w": w,
        "b": b,
    }
    grads = {
        "dw", dw,
        "db", db,
    }
    return params, grads, costs

def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)

    A = sigmoid(np.dot(w.T, X) + b)

    for i in range(A.shape[1]):
        Y_prediction[0][i] = 1 if A[0][i] >= 0.5 else 0

    assert(Y_prediction.shape == (1, m))
    return Y_prediction


        

