def isValidSubsequence(array, sequence):
    # Write your code here.
    s_index = 0

    for a in array:
        if s_index == len(sequence):
            break
        if a == sequence[s_index]:
            s_index += 1
    return s_index == len(sequence)