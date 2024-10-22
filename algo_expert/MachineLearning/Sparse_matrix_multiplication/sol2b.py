# check if the value in matrix_a[i][j] is 0. If it is, 
# skip the inner loop entirely (using continue).
# This avoids even looking at matrix_b[j][k]
# when matrix_a[i][j] == 0, thereby saving operations.
def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    
    # Initialize the output matrix with zeros.
    output = [[0 for _ in matrix_b[0]] for _ in matrix_a]
    
    # Perform matrix multiplication with optimized checks
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):  # Iterate over columns of matrix_a
            if matrix_a[i][j] == 0:  # If matrix_a[i][j] is 0, skip further checks
                continue
            
            for k in range(len(matrix_b[0])):  # Iterate over columns of matrix_b
                if matrix_b[j][k] != 0:  # Only multiply if matrix_b[j][k] is non-zero
                    output[i][k] += matrix_a[i][j] * matrix_b[j][k]

    return output
