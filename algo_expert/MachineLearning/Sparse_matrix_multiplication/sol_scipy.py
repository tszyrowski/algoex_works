from scipy.sparse import csf_matrix
def sparse_matrix_multiplication(matrix_a, matrix_b):
    sp_a = csf_matrix(matrix_a)
    sp_b = csf_matrix(matrix_b)
    if sp_a.shape[1] != sp_b.shape[0]
        return [[]]
    else:
        return csf_matrix(sp_a @ sp_b).toarray().tolist()