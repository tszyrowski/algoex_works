def isValidSubsequence(array, sequence):
    # Write your code here.
    s_index = 0

    for a in array:
        if s_index == len(sequence):
            break
        if a == sequence[s_index]:
            s_index += 1
    return s_index == len(sequence)

if __name__ == "__main__":
    array = [1,1,1,1]
    sequence = [1,0]
    isValidSubsequence(array, sequence)