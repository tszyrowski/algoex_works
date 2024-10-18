import time

def solution1(A): 
    # create a set to store the unique values in A 
    unique_set = set(A) 
  
    # start with 1 as the smallest positive number 
    smallest_val = 1
  
    # loop through the set and check for the smallest positive number 
    for i in range(len(unique_set)): 
        if smallest_val in unique_set: 
            smallest_val += 1
        else: 
            return smallest_val 
  
    return smallest_val

def solution2(A): 
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

def solution3(A): 
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

def solution4(A): 
    # create a binary search tree to store the values in A 
    bst = BinarySearchTree() 
  
    # start with 1 as the smallest positive number 
    smallest_val = 1
  
    # loop through the array and add the values to the binary search tree 
    for num in A: 
        if num > 0: 
            bst.insert(num)
  
    # loop through the binary search tree and check for the smallest positive number 
    while bbst.search(smallest_val) != None: 
        smallest_val += 1
  
    return smallest_val

def solution5(A): 
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

def solution6(A): 
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

# test case
A = [1, 3, 6, 4, 1, 2]

# solution 1
start_time = time.time()
result = solution1(A)
end_time = time.time()
print("Solution 1 Running Time: %.4f seconds" % (end_time - start_time))

# solution 2
start_time = time.time()
result = solution2(A)
end_time = time.time()
print("Solution 2 Running Time: %.4f seconds" % (end_time - start_time))

# solution 3
start_time = time.time()
result = solution3(A)
end_time = time.time()
print("Solution 3 Running Time: %.4f seconds" % (end_time - start_time))

# solution 4
start_time = time.time()
result = solution4(A)
end_time = time.time()
print("Solution 4 Running Time: %.4f seconds" % (end_time - start_time))

# solution 5
start_time = time.time()
result = solution5(A)
end_time = time.time()
print("Solution 5 Running Time: %.4f seconds" % (end_time - start_time))

# solution 6
start_time = time.time()
result = solution6(A)
end_time = time.time()
print("Solution 6 Running Time: %.4f seconds" % (end_time - start_time))