import dataclasses
import numpy as np
import matplotlib.pyplot as plt

import nn_utils


@dataclasses.dataclass
class DeepNeuralNetwork:
    X: np.array
    Y: np.array
    layer_dims: list or tuple
    learning_rate: float or int = 0.0075
    num_iterations: int = 3000
    print_cost: bool = False

    def __post_init__(self):
        self.m = len(self.X[1])
        self.parameters = {}

    def initialize_parameters(self):
        L = len(self.layer_dims) - 1  # number of layers in the network

        for l in range(1, L + 1):
            self.parameters['W' + str(l)] = np.random.randn(self.layer_dims[l], self.layer_dims[l - 1]) \
                                            / np.sqrt(self.layer_dims[l - 1])
            self.parameters['b' + str(l)] = np.zeros((self.layer_dims[l], 1))

            assert (self.parameters['W' + str(l)].shape == (self.layer_dims[l], self.layer_dims[l - 1]))
            assert (self.parameters['b' + str(l)].shape == (self.layer_dims[l], 1))

    def compute_loss(self, AL):
        cost = (1. / self.m) * (-np.dot(self.Y, np.log(AL).T) - np.dot(1 - self.Y, np.log(1 - AL).T))
        cost = np.squeeze(cost)
        assert (cost.shape == ())
        return cost

    def L_model_forward(self, X):
        caches = []
        A = X
        L = len(self.layer_dims) - 1  # number of layers in the neural network

        for l in range(1, L):
            A_prev = A
            A, cache = nn_utils.linear_activation_forward(
                A_prev,
                self.parameters['W' + str(l)],
                self.parameters['b' + str(l)],
                activation="relu"
            )
            caches.append(cache)

        AL, cache = nn_utils.linear_activation_forward(
            A,
            self.parameters['W' + str(L)],
            self.parameters['b' + str(L)],
            activation="sigmoid"
        )
        caches.append(cache)

        assert (AL.shape == (1, X.shape[1]))

        return AL, caches

    def L_model_backward(self, AL, caches):
        grads = {}
        L = len(self.layer_dims) - 1  # the number of layers
        Y = self.Y.reshape(AL.shape)  # after this line, Y is the same shape as AL

        dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))

        current_cache = caches[L - 1]
        grads["dA" + str(L)], grads["dW" + str(L)], grads["db" + str(L)] = \
            nn_utils.linear_activation_backward(dAL, current_cache, activation="sigmoid")

        for l in reversed(range(L - 1)):
            # lth layer: (RELU -> LINEAR) gradients.
            current_cache = caches[l]
            dA_prev_temp, dW_temp, db_temp = nn_utils.linear_activation_backward(
                grads["dA" + str(l + 2)], current_cache, activation="relu")

            grads["dA" + str(l + 1)] = dA_prev_temp
            grads["dW" + str(l + 1)] = dW_temp
            grads["db" + str(l + 1)] = db_temp

        return grads

    def update_parameters(self, grads):
        L = len(self.layer_dims) - 1

        # Update rule for each parameter. Use a for loop.
        for l in range(1, L + 1):
            self.parameters["W" + str(l)] = self.parameters["W" + str(l)] \
                                            - self.learning_rate * grads["dW" + str(l)]
            self.parameters["b" + str(l)] = self.parameters["b" + str(l)] \
                                            - self.learning_rate * grads["db" + str(l)]

    def run(self):
        costs = []
        self.initialize_parameters()
        for i in range(0, self.num_iterations):
            # Forward propagation: [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID.
            AL, caches = self.L_model_forward(self.X)
            # Compute cost.
            cost = self.compute_loss(AL)
            # Backward propagation.
            grads = self.L_model_backward(AL, caches)
            # Update parameters.
            self.update_parameters(grads)
            # Print the cost every 100 training example
            if self.print_cost and i % 100 == 0:
                print("Cost after iteration %i: %f" % (i, cost))
            if self.print_cost and i % 100 == 0:
                costs.append(cost)

        # plot the cost
        if self.print_cost:
            plt.plot(np.squeeze(costs))
            plt.ylabel('cost')
            plt.xlabel('iterations (per tens)')
            plt.title("Learning rate =" + str(self.learning_rate))
            plt.show()

    def predict(self, X, y):
        """
        This function is used to predict the results of a  L-layer neural network.

        Arguments:
        X -- data set of examples you would like to label
        parameters -- parameters of the trained model

        Returns:
        p -- predictions for the given dataset X
        """

        m = X.shape[1]
        p = np.zeros((1, m))

        # Forward propagation
        probas, caches = self.L_model_forward(X)

        # convert probas to 0/1 predictions
        for i in range(0, probas.shape[1]):
            if probas[0, i] > 0.5:
                p[0, i] = 1
            else:
                p[0, i] = 0

        # print results
        # print ("predictions: " + str(p))
        # print ("true labels: " + str(y))
        print("Accuracy: " + str(np.sum((p == y) / m)))

        return p

    @staticmethod
    def print_mislabeled_images(classes, X, y, p):
        """
        Plots images where predictions and truth were different.
        X -- dataset
        y -- true labels
        p -- predictions
        """
        a = p + y
        mislabeled_indices = np.asarray(np.where(a == 1))
        plt.rcParams['figure.figsize'] = (40.0, 40.0)  # set default size of plots
        num_images = len(mislabeled_indices[0])
        for i in range(num_images):
            index = mislabeled_indices[1][i]

            plt.subplot(2, num_images, i + 1)
            plt.imshow(X[:, index].reshape(64, 64, 3), interpolation='nearest')
            plt.axis('off')
            plt.title("Prediction: " + classes[int(p[0, index])].decode("utf-8") +
                      " \n Class: " + classes[y[0, index]].decode("utf-8"))


if __name__ == '__main__':
    train_X_orig, train_Y, test_X_orig, test_Y, classes = nn_utils.load_data()
    train_X = train_X_orig.reshape(train_X_orig.shape[0], -1).T / 255
    test_X = test_X_orig.reshape(test_X_orig.shape[0], -1).T / 255
    layers_dims = (train_X.shape[0], 7, 1)

    dnn = DeepNeuralNetwork(train_X, train_Y, layers_dims, num_iterations=1500, print_cost=True)
    dnn.run()
    predict = dnn.predict(test_X, test_Y)
    dnn.print_mislabeled_images(classes, test_X, test_Y, predict)
