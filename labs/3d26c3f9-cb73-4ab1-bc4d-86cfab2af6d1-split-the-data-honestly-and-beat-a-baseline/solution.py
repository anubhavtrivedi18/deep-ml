# --- cell 1 ---
import numpy as np


def split_and_baseline(X, y, train_frac, val_frac, test_frac, seed):
    """Split rows into train/val/test folds, fit something on the training fold, predict the test fold.

    Returns
    -------
    test_predictions : np.ndarray, shape (len(test_idx),)
    train_idx, val_idx, test_idx : 1-D integer arrays forming a partition of range(len(y))
    """
    rng = np.random.default_rng(seed)
    indices = np.arange(len(y))
    rng.shuffle(indices)
    n_train = int(len(y)*train_frac)
    n_val = int(len(y)*val_frac)
    x_test = len(y)-n_train-n_val
    train_idx = indices[:n_train]
    val_idx = indices[n_train:n_train + n_val]
    test_idx = indices[n_train + n_val:]
    mean = np.mean(y[train_idx])
    test_predictions = np.full(len(test_idx), mean)
    return test_predictions,train_idx,val_idx,test_idx

# --- cell 2 ---
import numpy as np


def split_and_baseline(X, y, train_frac, val_frac, test_frac, seed):
    """Split rows into train/val/test folds, fit something on the training fold, predict the test fold.

    Returns
    -------
    test_predictions : np.ndarray, shape (len(test_idx),)
    train_idx, val_idx, test_idx : 1-D integer arrays forming a partition of range(len(y))
    """
    rng = np.random.default_rng(seed)
    indices = np.arange(len(y))
    rng.shuffle(indices)
    n_train = int(len(y)*train_frac)
    n_val = int(len(y)*val_frac)
    x_test = len(y)-n_train-n_val
    train_idx = indices[:n_train]
    val_idx = indices[n_train:n_train + n_val]
    test_idx = indices[n_train + n_val:]
    mean = np.mean(y[train_idx])
    test_predictions = np.full(len(test_idx), mean)
    return test_predictions,train_idx,val_idx,test_idx