import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Your code here
    AtA = A.T@A
    theta = 0.5*np.arctan((2*AtA[0,1])/(AtA[0,0]-AtA[1,1]))
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.array([[c,-s],[s,c]])
    D = R.T@(A.T@A)@R 
    V = R 
    summation_inverse = np.array([
    [1/np.sqrt(D[0,0]), 0],
    [0, 1/np.sqrt(D[1,1])]
])
    U = A @ V @ summation_inverse
    S = np.array([np.sqrt(D[0,0]),np.sqrt(D[1,1])])
    S = np.sort(S)[::-1]
    return (U,S,V.T)