import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.
    
    Args:
        A: Square matrix as a list of lists
    
    Returns:
        tuple: (L, U) where L is lower triangular with 1s on diagonal,
               U is upper triangular, and A = L @ U
    """
    # Your code here
    A = np.array(A)
    rows = A.shape[0]
    columns = A.shape[1]
    U = np.zeros((rows,columns))
    L = np.zeros((rows,columns))
    for i in range(rows):
        for j in range(columns):
            if i<=j:
                total = 0
                for k in range(i):
                    total+=L[i][k]*U[k][j]
                U[i][j]=A[i][j]-total
            else:
                total = 0
                for k in range(j):
                    total+=L[i][k]*U[k][j]
                L[i][j] = (A[i][j]-total)/U[j][j]
        L[i][i]=1
    return L,U