import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    for epochs in range(n_iter):
        i = epochs%(len(X))
        y_predict = X[i]@weights
        loss = (y_predict-y[i])**2
        gradient = 2*(y_predict-y[i])*X[i]
        weights = weights-learning_rate*gradient 
    return weights