# O(n^3) time (no check for 0)
def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Write your code here.
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    else:
        # output = [[[0]*len(matrix_a)]*len(matrix_b[0])]
        output = [[0 for i in matrix_b[0]] for j in matrix_a]
        for i in range(len(matrix_a)):
            for k in range(len(matrix_b[0])):  # Iterate over columns of matrix_b
                for j in range(len(matrix_b)):  # Iterate over the rows of matrix_b
                    output[i][k] += matrix_a[i][j] * matrix_b[j][k]
        return output
