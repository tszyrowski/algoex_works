def transposeMatrix(matrix):
    """
    Returns the transpose of the given 2D matrix.
    
    :param matrix: List of lists where each inner list is a row of the matrix
    :return: Transposed version of the matrix
    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

if __name__ == "__main__":
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    t = transposeMatrix(matrix)
    print(t)
