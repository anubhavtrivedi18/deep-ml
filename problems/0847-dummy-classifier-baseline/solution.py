import numpy as np
from collections import Counter

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    if strategy=="most_frequent":
        values,counts = np.unique(y_train,return_counts = True)
        index = np.argmax(counts)
        number = values[index]
        return [number]*n_test
    elif strategy=="constant":
        return [constant]*n_test
    elif strategy=="uniform":
        sorted_values = np.sort(y_train)
        values = np.unique(sorted_values)
        k = len(values)
        return [np.arange(n_test)%k]
    else:
        values,counts = np.unique(y_train,return_counts = True)
        frequencies = counts / len(y_train)
        expected = n_test * frequencies
        allocation = np.floor(expected).astype(int)
        remaining = n_test - np.sum(allocation)
        fractional = expected - allocation
        order = np.argsort(-fractional)
        for i in range(remaining):
            allocation[order[i]] += 1
        predictions = []
        for value, count in zip(values, allocation):
            predictions.extend([value] * count)
        return predictions  
