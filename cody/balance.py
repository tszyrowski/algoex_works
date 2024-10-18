def solution(R, V):
    # Implement your solution here
    balanceA = 0
    needA = 0
    balanceB = 0
    needB = 0
    for i in range(len(R)):
        if R[i] == 'A':
            balanceA += V[i]
            balanceB -= V[i]
            if balanceA < 0 :
                needA += (-balanceA)
            if balanceB < 0 :
                needB += (-balanceB)
        else:
            balanceA -= V[i]
            balanceB += V[i]
            if balanceA < 0 :
                needA += (-balanceA)
            if balanceB < 0 :
                needB += (-balanceB)
    return [needA, needB]

sol = solution('BAABA', [2, 4, 1, 1, 2])
print("expected [2, 4] got: ", sol)
sol = solution('ABAB', [10, 5, 10, 15])
print("expected [0, 15] got: ", sol)
sol = solution('B', [100])
print("expected [100, 0] got: ", sol)