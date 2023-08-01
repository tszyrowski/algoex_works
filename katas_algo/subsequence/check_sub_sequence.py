def isValidSubsequence(array, sequence):
    # Write your code here.
    order = []
    # Check if all elements of sequense in array
    for s in sequence:
        print(s)
        try:
            order.append(array.index(s))
        except ValueError:
            return False
    for i in range(0,len(order)-1):
        if order[i] >= order[i+1]:
            return False
    return True

if __name__ == "__main__":
    array = [1,1,1,1]
    sequence = [1,1,1]
    t = isValidSubsequence(array, sequence)
    print(t)