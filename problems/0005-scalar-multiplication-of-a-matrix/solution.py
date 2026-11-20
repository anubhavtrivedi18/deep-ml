def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = [ ]
    # Your code here
    for row in matrix:
        new_row = [ ]
        for element in row:
            new_row.append(element*scalar)
        result.append(new_row)
        
    return result