def transposeMatrix(matrix):
    # initialise with the rows and columns in trans order
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose [j][i] = matrix[i][j]

    return transpose

if __name__ == "__main__":
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    t = transposeMatrix(matrix)
    print(t)