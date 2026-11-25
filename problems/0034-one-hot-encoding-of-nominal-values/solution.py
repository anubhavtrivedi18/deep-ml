import numpy as np

def to_categorical(x, n_col=None):
    # Your code here
    if n_col is None:
        n_col = max(x)+1

    matrix = np.zeros((len(x),n_col))
    for i in range(len(x)):
        matrix[i,x[i]] = 1
    return matrix