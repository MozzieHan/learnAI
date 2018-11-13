import numpy as np
import nn_utils

class DeepNeuralNetwork:
    def __init__(self, X, Y, layer_dims, alpha=0.0075, num_iterations=10000):
        """
        :param X: shape = (n_x, m)
        :param Y: shape = (1, m) # 对于单输出来说
        :param layers_dims: list [n_x, n_1, n_2, ... , n_l]
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
            self.parameters["b" + str(l)] = np.zeros(self.layer_dims[l])

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
        pass

    def line_backward(self):
        pass

    def L_model_backward(self):
        pass

    def update_parameters(self):
        pass

    def compute_cost(self, AL):
        assert(AL.shape == self.Y.shape)
        cost = -1/self.m * (np.divide(self.Y, np.log(AL)) + np.divide((1-self.Y), np.log(1-AL)))
        return cost

    def run(self):
        pass

if __name__ == '__main__':
    X = np.random.randn(64 * 64 * 3, 200)
    Y = np.random.randint(0, 2, (1, 200))
    print(Y)
    neural_network = DeepNeuralNetwork(X, Y, (3,4,5,6,1))
    neural_network.initialize_parameters()

