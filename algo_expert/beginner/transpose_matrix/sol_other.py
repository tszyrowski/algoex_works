def transposeMatrix(matrix):
    return list(zip(*matrix))


def transposeMatrix(matrix):
    return [list(t) for t in list(zip(*matrix))] 

def transposeMatrix(matrix):
    res = [[] for i in range(len(matrix[0]))]
    for i in matrix:
        for idx, val in enumerate(i):
            res[idx].append(val)
    return res