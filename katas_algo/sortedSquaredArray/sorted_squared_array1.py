"""Return sorted array of squares from sorted input array

Complexity: o(n) time | O(n) space where n is length of input array

1. `sortedSquaredArray(array)`:
   This function works by two pointers, starting at both ends of 
   the sorted array and gradually closing in towards the middle. 
   It compares absolute values of array elements at the pointers and selects 
   the larger one to square and place in the resultant array. 
   This process is done in-place and doesn't require additional space. 
   Therefore, the function operates in O(1) space complexity.
   
   For time complexity, each element in the array is processed once, 
   so the function operates in O(n) time complexity, 
   where n is the length of the input array.

2. `sortedSquaredArray1(array)`:

   This function squares each element in the array and then sorts the array. 
   The squaring operation is O(n), and the sort operation is typically 
   O(n log n) (as implemented in Python's `sorted` function, 
   which uses a version of Timsort). 
   Hence, the overall time complexity is dominated by the sorting operation, 
   making it O(n log n).
   
   Regarding space complexity, the list comprehension creates a new list which 
   requires O(n) space. Furthermore, Python's sorting algorithm also uses O(n) 
   space, so the total space complexity of this function is O(n).

To conclude, the first function `sortedSquaredArray` is more efficient, 
with a time complexity of O(n) and a space complexity of O(1), 
compared to the second function `sortedSquaredArray1`, 
which has a time complexity of O(n log n) and a space complexity of O(n).
"""
def sortedSquaredArray(array):
    # pointer to biggest, sorting in single go
    output = [0]*len(array)
    min_t = 0               # start
    max_t = len(array) - 1  # end
    i = len(array) - 1      # we will be adding to the end of the array 
    while min_t <= max_t:
        if abs(array[min_t]) > abs(array[max_t]): # check if start or end bigger
            output[i] = array[min_t]**2
            min_t += 1
        else:
            output[i] = array[max_t]**2
            max_t -= 1
        i -= 1
    return output

def sortedSquaredArray1(array):
    # Not optimal as sorting after squaring
    # O(n_log_n) time | O(n) space
    return sorted([a**2 for a in array])

if __name__ == "__main__":
    array = [
        [1, 2, 3, 5, 6, 8, 9],
        [1, 2],
        [1, 2, 3, 4, 5],
        [0],
        [10],
        [-1],
        [-2, -1],
        [-5, -4, -3, -2, -1],
        [-10],
        [-10, -5, 0, 5, 10],
        [-7, -3, 1, 9, 22, 30],
        [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, -1, 2, 3, 3, 3, 4],
        [-3, -2, -1]
    ]

    expected = [
        [1, 4, 9, 25, 36, 64, 81],
        [1, 4],
        [1, 4, 9, 16, 25],
        [0],
        [100],
        [1],
        [1, 4],
        [1, 4, 9, 16, 25],
        [100],
        [0, 25, 25, 100, 100],
        [1, 9, 49, 81, 484, 900],
        [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 4, 9, 9, 9, 16],
        [1, 4, 9]
    ]
    
    for i in range(len(array)):
        output = sortedSquaredArray(array[i])
        print(f"{i+1}: {output}, -> {expected[i]}")
        assert output == expected[i]

    # TIME COMPLEXITY
    import time
    # Generate a large list for testing
    import random
    test_array = sorted([random.randint(-100000, 100000) for _ in range(1000000)])

    # Measure time for sortedSquaredArray
    start = time.time()
    sortedSquaredArray(test_array)
    end = time.time()
    print(f"Time taken by sortedSquaredArray: {end - start} seconds")

    # Measure time for sortedSquaredArray1
    start = time.time()
    sortedSquaredArray1(test_array)
    end = time.time()
    print(f"Time taken by sortedSquaredArray1: {end - start} seconds")

    # SPACE COMPLEXITY
    import gc
    from memory_profiler import memory_usage

    # Measure memory usage for sortedSquaredArray
    gc.collect()
    start_mem = memory_usage()[0]
    sortedSquaredArray(test_array)
    end_mem = memory_usage()[0]
    print(f"Memory used by sortedSquaredArray: {end_mem - start_mem} MiB")

    # Measure memory usage for sortedSquaredArray1
    gc.collect()
    start_mem = memory_usage()[0]
    sortedSquaredArray1(test_array)
    end_mem = memory_usage()[0]
    print(f"Memory used by sortedSquaredArray1: {end_mem - start_mem} MiB")

    """
    Space analysis is incorrect, but running it twice gives different results
    As for the memory usage, the negative value for sortedSquaredArray1 
    is curious and might suggest that Python's garbage collector ran during 
    the execution of that function, freeing up some memory. The memory_usage() 
    function measures the total memory usage of Python process, 
    not just the memory used by the function you're testing. 
    If some other part of program is freeing up memory while function is running, 
    you might see a decrease in total memory usage.
    """