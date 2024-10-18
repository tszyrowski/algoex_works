# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # Implement your solution here
#     val = 1
#     if val in set(A):
#         val += 1
#     else:
#         return val

def solution(A): 
    """Find first smallest number not in list"""
    set_A = set(A) 
    val = 1

    for i in range(len(set_A)): 
        if val in set_A: 
            val += 1
        else: 
            return val 
  
    return val
#he time complexity of the above solution can be reduced by using a hashmap instead of a set. This will reduce the time complexity from O(N) to O(N/2).
def solution_hash(A): 
    # create a hashmap to store the values in A 
    num_map = {} 
  
    # start with 1 as the smallest positive number 
    smallest_val = 1
  
    # loop through the array and add the values to the hashmap 
    for num in A: 
        if num > 0: 
            num_map[num] = 1
  
    # loop through the hashmap and check for the smallest positive number 
    for i in range(len(num_map)): 
        if smallest_val in num_map: 
            smallest_val += 1
        else: 
            return smallest_val 
  
    return smallest_val
# the time complexity of the above solution can be further reduced by using a bitmap instead of a hashmap. This will reduce the time complexity from O(N/2) to O(log N).
def solution_bitmap(A): 
    # create a bitmap to store the values in A 
    bitmap = 0
  
    # start with 1 as the smallest positive number 
    smallest_val = 1
  
    # loop through the array and add the values to the bitmap 
    for num in A: 
        if num > 0: 
            bitmap |= (1 << num)
  
    # loop through the bitmap and check for the smallest positive number 
    for i in range(len(bitmap)): 
        if smallest_val & bitmap == 0: 
            return smallest_val 
        else: 
            smallest_val += 1
  
    return smallest_val
#the time complexity of the above solution can be further reduced by using a binary search tree instead of a bitmap. This will reduce the time complexity from O(log N) to O(log N log N).
def solution_binary_search(A): 
    # create a binary search tree to store the values in A 
    bst = BinarySearchTree() 
  
    # start with 1 as the smallest positive number 
    smallest_val = 1
  
    # loop through the array and add the values to the binary search tree 
    for num in A: 
        if num > 0: 
            bst.insert(num)
  
    # loop through the binary search tree and check for the smallest positive number 
    while bst.search(smallest_val) != None: 
        smallest_val += 1
  
    return smallest_val
#the time complexity of the above solution can be further reduced by using a priority queue instead of a binary search tree. This will reduce the time complexity from O(log N log N) to O(N log N).
def solution_prior_queue(A): 
    # create a priority queue to store the values in A 
    pq = PriorityQueue() 
  
    # start with 1 as the smallest positive number 
    smallest_val = 1
  
    # loop through the array and add the values to the priority queue 
    for num in A: 
        if num > 0: 
            pq.add(num)
  
    # loop through the priority queue and check for the smallest positive number 
    while pq.peek() != None: 
        if smallest_val == pq.peek(): 
            pq.remove() 
            smallest_val += 1
        else: 
            return smallest_val 
  
    return smallest_val

# the time complexity of the above solution can be further reduced by using a balanced binary search tree instead of a priority queue. This will reduce the time complexity from O(N log N) to O(N).

def solution(A): 
    # create a balanced binary search tree to store the values in A 
    bbst = BalancedBinarySearchTree() 
  
    # start with 1 as the smallest positive number 
    smallest_val = 1
  
    # loop through the array and add the values to the balanced binary search tree 
    for num in A: 
        if num > 0: 
            bbst.insert(num)
  
    # loop through the balanced binary search tree and check for the smallest positive number 
    while bbst.search(smallest_val) != None: 
        smallest_val += 1
  
    return smallest_val


# For the first solution, the time complexity is O(N) where N is the number of elements in the array. This is because we loop through the set to check for the smallest positive number.

# For the second solution, the time complexity is O(N/2) where N is the number of elements in the array. This is because we loop through the hashmap to check for the smallest positive number, and the lookup time for a hashmap is constant, meaning that it takes the same amount of time regardless of the size of the map.

# For the third solution, the time complexity is O(log N) where N is the number of elements in the array. This is because we loop through the bitmap to check for the smallest positive number, and the lookup time for a bitmap is logarithmic, meaning that it takes less time to search through a larger bitmap.

# For the fourth solution, the time complexity is O(log N log N) where N is the number of elements in the array. This is because we loop through the binary search tree to check for the smallest positive number, and the lookup time for a binary search tree is logarithmic, meaning that it takes less time to

if __name__ == "__main__":
    A = [1, 2, 3]
    v = solution(A)
    print(v)
    A = [1, 3, 6, 4, 1, 2]
    v = solution(A)
    print(v)
    A = [-1, -3]
    v = solution(A)
    print(v)