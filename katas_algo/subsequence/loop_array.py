def isValidSubsequence(array, sequence):
    sequence_copy = sequence.copy()
    order = []
    for a in array:
        try:
            s_i = sequence.index(a)
            order.append(a)
            sequence.pop(s_i)
        except ValueError:
            continue

    return True if sequence_copy == order else False