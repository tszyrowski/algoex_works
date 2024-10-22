# Multiplying by zero doesn't change the result,
# so there's no point in performing the operation.
# By skipping these multiplications,
# we reduce the total number of operations.
def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    output = [[0 for _ in matrix_b[0]] for _ in matrix_a]
    for i in range(len(matrix_a)):
        for k in range(len(matrix_b[0])):
            for j in range(len(matrix_b)):
                if matrix_a[i][j] != 0 and matrix_b[j][k] != 0:
                    output[i][k] += matrix_a[i][j] * matrix_b[j][k]
    return output