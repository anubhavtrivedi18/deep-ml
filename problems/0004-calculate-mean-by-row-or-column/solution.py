def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = [ ]
    if mode == "row":
        for row in matrix:
            mean = 0
            for element in row:
                mean+=element
            mean = mean/len(row)
            means.append(mean)
    else:
        for column in zip(*matrix):
            mean = 0 
            for element in column:
                mean+=element
            mean = mean/len(column)
            means.append(mean)
    return means