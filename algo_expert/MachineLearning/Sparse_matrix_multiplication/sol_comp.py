def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    matrix_p = [[0]*len(matrix_b[0]) for _ in matrix_a]
    for col_a in range(len(matrix_a[0])):
        non_zeros_in_b = [[col_b, v_b] for col_b, v_b in enumerate(matrix_b[col_a]) if v_b]
        for row_a in (_ for _ in range(len(matrix_a)) if matrix_a[_][col_a]):
            for col_b, v_b in non_zeros_in_b:
                matrix_p[row_a][col_b] += matrix_a[row_a][col_a] * v_b
    return matrix_p
