from sol_comp import sparse_matrix_multiplication

def test_mat_mult_1():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0, 2, 0],
            [0, -3, 5]
        ],
        "matrix_b": [
            [0, 10, 0],
            [0, 0, 0],
            [0, 0, 4]
        ]
    }
    expected = [
        [0, 0, 0],
        [0, 0, 20]
    ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_2():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [46, 0, 0],
            [45, 47, 0],
            [0, 0, 0],
            [34, 0, 25],
            [0, 2, 0],
            [0, 0, 0]
        ],
        "matrix_b": [
            [26, 34, 20, 31, 34, 15],
            [38, 30, 23, 1, 45, 22],
            [47, 9, 9, 5, 9, 31]
        ]
        }
    expected = [
        [1196, 1564, 920, 1426, 1564, 690],
        [2956, 2940, 1981, 1442, 3645, 1709],
        [0, 0, 0, 0, 0, 0],
        [2059, 1381, 905, 1179, 1381, 1285],
        [76, 60, 46, 2, 90, 44],
        [0, 0, 0, 0, 0, 0]
        ]


    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_3():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0, 0, 1],
            [1, 0, 2],
            [0, 0, 1]
        ],
        "matrix_b": [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0]
        ]
        }
    expected = [
        [0, 1, 0],
        [0, 3, 0],
        [0, 1, 0]
        ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_4():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0]
        ],
        "matrix_b": [
            [0]
        ]
        }
    expected = [
        [0]
        ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_5():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0, 0, 0, 0, 0, 2, 0, 0]
        ],
        "matrix_b": [
            [0],
            [0],
            [0],
            [0],
            [0],
            [3],
            [0],
            [0]
        ]
        }
    expected = [
        [6]
        ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_6():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0],
            [0],
            [0],
            [0],
            [0],
            [3],
            [0],
            [0]
        ],
        "matrix_b": [
            [0, 0, 0, 0, 0, 2, 0, 0]
        ]
        }
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
        ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_7():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [-7, 0, 0],
            [0, 0, 0],
            [0, 2, 0],
            [2, 0, 0],
            [0, 0, 0],
            [0, 0, 9],
            [0, 0, 0],
            [6, -1, 7],
            [0, 0, 0],
            [0, 0, 0],
            [0, -8, 0]
        ],
        "matrix_b": [
            [3, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        }

    expected = [
        [-21, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [6, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [18, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_8():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0, 0, 0, 0, 0, -1, 3, 0, 0, 0, 0, 0, -4, 0],
            [-2, 0, 0, 0, 7, -2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 7, 0],
            [0, 0, 0, 2, 0, 3, 0, -2, -2, 0, 0, 0, -6, 0],
            [0, 0, 0, 0, 0, -9, 0, 0, 0, 0, 0, 9, 0, 0],
            [1, 0, -9, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
            [0, -9, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, -6, 4, 0, 5, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, -7, -7, 0, 5, 0, 0],
            [0, 0, 0, 0, 5, -2, 0, 0, -8, 0, 0, 0, 0, 0],
            [-6, 0, 0, 5, 0, 9, 0, -5, 0, 9, 0, 0, 0, 0]
        ],
        "matrix_b": [
            [0, 0],
            [0, 0],
            [-8, 0],
            [4, 0],
            [0, 0],
            [0, 0],
            [2, 8],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 0],
            [3, 0],
            [0, 0],
            [0, 0],
            [0, 0]
        ]
        }
    expected = [[]]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_9():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 8, 0, 0, 0, -4, 0],
            [0, 0, 0, -3, 0, 4, -5, 0, 0, -2, 0],
            [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, -6, 0, 0, 0, -7, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, -9, 0, 0, 0],
            [0, 0, 0, -4, 0, 6, 0, 0, 0, 0, 0],
            [0, -4, 0, 0, 0, 0, -4, 0, 0, 0, 0],
            [0, 0, -9, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        "matrix_b": [
            [0, 6, -5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
            [0, -9, -3, 0, 0, 0, 0, 0, 0, -9, 0, 0, 0, 0],
            [0, -9, 0, 0, 0, -2, 7, 0, 8, 5, 0, -2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 0, -4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -7, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, -1, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, -2, 3, -5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0],
            [0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, -6, 0, -1]
        ]
        }
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 32, -8, 0, 16, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 10, -4, -3, 8, 0, 0, 0],
        [0, -12, 10, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [-56, 48, -40, 24, 0, 0, 0, -6, 14, -21, 35, 0, 42, -8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 16, -6, 16, 0, 0, 0, 0],
        [0, 36, 12, 0, 0, 0, 4, 0, 0, 24, 0, 0, 0, 0],
        [0, 81, 0, 0, 0, 18, -63, 0, -72, -45, 0, 18, 0, 0]
        ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_10():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-5, -9, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 5, -4, -3, 0],
            [0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0],
            [0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 6, 0],
            [0, 0, 0, 0, 9, 0, 3, 4, 0, 0, 0, 0]
        ],
        "matrix_b": [
            [3, 0],
            [0, 0],
            [8, 0],
            [7, 0],
            [-8, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 8],
            [0, 0],
            [0, 0],
            [0, 0]
        ]
        }
    expected = [
        [0, 0],
        [-71, 0],
        [0, 0],
        [0, 40],
        [0, 0],
        [-64, 0],
        [-72, 0]
        ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_mat_mult_11():
    # Load the graph data from the JSON input.
    input = {
        "matrix_a": [
            [0, 0, 0, 0, 0, 0, -5, 0, 2, 0, 0, 0, 0, -1, 0, 0, 0, 3, 0, 0],
            [0, 0, 0, 0, 7, -5, 0, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 0, 0, 0, -8, 0, -3, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, -1, 0, -3, 0, -6, 0],
            [0, 0, -3, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, -3, 6, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0],
            [0, 0, 0, 9, 0, 7, 0, 0, -6, 0, 0, 6, 0, 0, 3, 0, 0, 0, 0, 7],
            [0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [5, 0, 0, 0, -2, -2, -4, 0, -5, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -7, 0, 3, 2, 0],
            [0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9, 1, 0, 0, 0, 0],
            [0, -3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, 0],
            [2, 0, 0, 5, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-2, 0, 1, 0, 0, 0, 0, 8, -9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, -8, 0, 0, -4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, -9, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 8, 0, 0, 5, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, -9, 0, -4, 8, 0, 0, -9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, -3, -7, 7, 0, 0, 0, 3, -5, 0, 0, 0, 0]
        ],
        "matrix_b": [
            [0, -7, 1, 0, 3],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, -6, -3],
            [0, 0, 0, 0, 0],
            [0, 3, 0, 0, 0],
            [0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, -4],
            [0, 0, 0, 0, -9],
            [-2, 0, 0, 9, 0],
            [0, -9, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, -5, 0, 0],
            [0, 0, 0, 0, -9],
            [0, 0, -5, 0, 8],
            [0, 0, 0, 0, -2],
            [0, 4, 0, 0, 0],
            [0, 0, 0, 9, 0],
            [0, 0, -1, 2, 0]
        ]
        }
    expected = [
        []
        ]

    result = sparse_matrix_multiplication(input["matrix_a"], input["matrix_b"])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"


if __name__ == "__main__": 
    import pytest
    pytest.main(["-s", "-v", __file__])