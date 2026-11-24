import numpy as np

def classify_critical_point(hessian: np.ndarray, tol: float = 1e-10):
    eigen_values = np.linalg.eigvals(hessian)
    if np.all((eigen_values)>tol):
        return -1
    elif np.all((eigen_values)<-tol):
        return 1
    elif np.any((eigen_values >= -tol) & (eigen_values <= tol)):
        return None
    else:
        return 0