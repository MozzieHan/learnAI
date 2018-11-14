import numpy as np
import nn_utils


class DeepNeuralNetwork:
    def __init__(self, X, Y, layer_dims, alpha=0.0075, num_iterations=10000):
        """
        :param X: shape = (n_x, m)
        :param Y: shape = (1, m) # 对于单输出来说
        :param layer_dims: list [n_x, n_1, n_2, ... , n_l]
        :param alpha: float
        :param num_iterations: int
        """
        self.X = X
        self.Y = Y
        self.layer_dims = layer_dims
        self.alpha = alpha
        self.num_iterations = num_iterations
        self.m = X.shape[1]
        self.layer_num = len(layer_dims) - 1
        self.parameters = {}

    def initialize_parameters(self):
        for l in range(1, self.layer_num + 1):
            self.parameters["W" + str(l)] = np.random.randn(self.layer_dims[l], self.layer_dims[l-1])
            self.parameters["b" + str(l)] = np.zeros((self.layer_dims[l], 1))

    def line_forward(self, W, b, A_pre, activation):
        """
        :param W:
        :param b:
        :param A_pre:
        :return:
        """
        Z = np.dot(W, A_pre) + b
        if activation == "sigmoid":
            A = nn_utils.sigmoid(Z)
        elif activation == "relu":
            A = nn_utils.relu(Z)
        else:
            raise KeyError

        return A, Z, (W, b, A_pre)

    def L_model_forward(self):
        A_pre = self.X
        A_cache = [A_pre]
        for l in range(1, self.layer_num):
            A, Z, cache = self.line_forward(
                self.parameters["W" + str(l)],
                self.parameters["b" + str(l)],
                A_pre,
                "relu"
            )
            A_pre = A
            A_cache.append(A_pre)
        AL, ZL, cache = self.line_forward(
            self.parameters["W" + str(self.layer_num)],
            self.parameters["b" + str(self.layer_num)],
            A_pre,
            "sigmoid"
        )

        A_cache.append(AL)
        return AL, A_cache

    def line_backward(self, dZ, A_pre):
        dW = 1/self.m * np.dot(dZ, A_pre.T)
        db = 1/self.m * np.sum(dZ, axis=1, keepdims=True)
        dA_pre = np.dot(W.T, dZ)
        return dW, db, dA_pre

    def L_model_backward(self, AL, A_cache):
        grads = {}
        dZ = AL - self.Y
        A_pre = A_cache[self.layer_num - 1]
        dW, db, dA_pre = self.line_backward(dZ, A_pre)
        grads["dW" + str(self.layer_num)] = dW
        grads["db" + str(self.layer_num)] = db

        for l in range(self.layer_num - 1, 0, -1):
            dZ = np.dot(self.parameters["W" + str(l)].T, dA)
            A_pre = A_cache[l-1]
            dW, db, dA_pre = self.line_backward(dZ, A_pre)
            grads["dW" + str(l)] = dW
            grads["db" + str(l)] = db

    def update_parameters(self, grads):
        for l in range(1, self.layer_num + 1):
            self.parameters["W" + str(l)] -= self.alpha * grads["dW" + str(l)]
            self.parameters["b" + str(l)] -= self.alpha * grads["db" + str(l)]

    def compute_cost(self, AL):
        assert(AL.shape == self.Y.shape)
        cost = -1/self.m * (np.dot(self.Y, np.log(AL.T)) +
                            np.dot((1-self.Y), np.log(1-AL.T)))
        cost = np.squeeze(cost)
        return cost

    def run(self):
        pass


if __name__ == '__main__':
    X = np.random.rand(64 * 64 * 3, 200)
    Y = np.random.randint(0, 2, (1, 200))

    neural_network = DeepNeuralNetwork(X, Y, (64 * 64 * 3, 4, 5, 6, 1))
    neural_network.initialize_parameters()
    AL, A_cache = neural_network.L_model_forward()
    cost = neural_network.compute_cost(AL)
    print(cost)


