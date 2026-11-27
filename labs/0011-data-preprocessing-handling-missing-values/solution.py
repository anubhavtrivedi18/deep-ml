# --- cell 1 ---
import numpy as np

def impute(X: np.ndarray) -> np.ndarray:
    '''
    Fill in missing values (NaN) in the input array.
    '''
    X_clean = X.copy()
    for j in range(X.shape[1]):
        col = X[:, j]
        valid = col[~np.isnan(col)]
        if len(valid) == 0:
            X_clean[:, j] = 0
            continue
        mean = np.mean(valid)
        std = np.std(valid)
        if std == 0:
            skew = 0
        else:
            skew = np.mean((valid - mean) ** 3) / std ** 3
        if -0.5 <= skew <= 0.5:
            fill_value = mean
        else:
            fill_value = np.median(valid)
        X_clean[np.isnan(col), j] = fill_value
    return X_clean