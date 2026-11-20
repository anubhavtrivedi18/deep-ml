def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    i = len(a)
    j = len(a[0])
    matrix = [[1]*i for _ in range(j)]
    for l in range(i):
        for k in range(j):
            matrix[k][l] = a[l][k]
    return matrix 