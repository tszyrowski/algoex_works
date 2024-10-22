# Time O(nz) where nz is the number of non-zero elements

# preprocess both matrices by storing the non-zero elements in a more compact form
# (e.g., a dictionary with keys being their indices
# and values being the non-zero entries). This preprocessing would allow you to only perform multiplications on the non-zero entries. Here's an idea for that:

# Preprocessing the Matrices
# Instead of iterating over all elements in matrix_a and matrix_b,
# we can first extract the non-zero entries and only perform the multiplication
# for these.

# This concept of DICTIONARY OF LEYS
def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    
    # Preprocess matrix_a to get non-zero elements
    non_zero_a = {}
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            if matrix_a[i][j] != 0:
                if i not in non_zero_a:
                    non_zero_a[i] = {}
                non_zero_a[i][j] = matrix_a[i][j]
    
    # Preprocess matrix_b to get non-zero elements
    non_zero_b = {}
    for j in range(len(matrix_b)):
        for k in range(len(matrix_b[0])):
            if matrix_b[j][k] != 0:
                if j not in non_zero_b:
                    non_zero_b[j] = {}
                non_zero_b[j][k] = matrix_b[j][k]
    
    # Initialize the output matrix with zeros.
    output = [[0 for _ in matrix_b[0]] for _ in matrix_a]
    
    # Perform multiplication only for non-zero elements
    for i in non_zero_a:
        for j in non_zero_a[i]:
            if j in non_zero_b:  # Check if there is a corresponding non-zero column in matrix_b
                for k in non_zero_b[j]:
                    output[i][k] += non_zero_a[i][j] * non_zero_b[j][k]

    return output
