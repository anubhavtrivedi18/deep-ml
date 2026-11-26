
import numpy as np

def rmse(y_true, y_pred):
    # Write your code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    if y_true.shape != y_pred.shape or (len(y_true)==0 and len(y_pred) == 0):
        raise ValueError
    else:
        mse = np.mean((y_true-y_pred)**2)
        rmse_res = np.sqrt(mse)
        return round(rmse_res,3)