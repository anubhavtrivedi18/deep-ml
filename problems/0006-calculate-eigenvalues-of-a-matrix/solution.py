def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    trace = matrix[0][0]+matrix[1][1]
    eigenvalues = [ ]
    d = (trace**2-4*1*det)**(1/2)
    eigen_1 = (-(-trace)-d)/2
    eigen_2 = (-(-trace)+d)/2
    eigenvalues.extend([eigen_1,eigen_2])
    eigenvalues.sort(reverse=True)
    return eigenvalues