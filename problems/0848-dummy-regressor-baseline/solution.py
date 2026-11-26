import numpy as np

def dummy_regressor(y_train, n_test, strategy='mean', constant=None, quantile=None):
    """
    Baseline regressor that predicts a constant value derived from y_train.

    Args:
        y_train: 1D array-like of training target values.
        n_test: number of test predictions to return (int >= 0).
        strategy: one of 'mean', 'median', 'quantile', 'constant'.
        constant: required when strategy='constant'.
        quantile: required when strategy='quantile', must be in [0, 1].

    Returns:
        List[float] of length n_test, all equal to the chosen summary value.
    """
    if strategy =="mean":
        mean = np.mean(y_train)
        return [mean]*n_test
    elif strategy == "median":
        median = np.median(y_train)
        return [median]*n_test
    elif strategy == "constant":
        if constant is None:
            raise ValueError
        else:
            return [constant]*n_test
    elif strategy == "quantile":
        if quantile is None:
            raise ValueError
        else:
            quantile_value = np.quantile(y_train,quantile)
            return [quantile_value]*n_test
    else:
        raise ValueError