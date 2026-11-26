import numpy as np

def mini_batch_gd_step(
    X: np.ndarray,
    y: np.ndarray,
    weights: np.ndarray,
    bias: float,
    batch_indices: list,
    lr: float
) -> np.ndarray:
    x = X[batch_indices]
    m = len(batch_indices)

    y_batch = y[batch_indices]

    y_predict = x @ weights + bias

    error = y_predict - y_batch

    gradient_weights = 2 * (error @ x) / m
    gradient_bias = 2 * np.sum(error) / m

    weights = weights - lr * gradient_weights
    bias = bias - lr * gradient_bias

    return np.append(weights, bias)