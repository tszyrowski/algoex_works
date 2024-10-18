def solution(X, Y, A):
    N = len(A)
    result = -1
    nX = 0
    nY = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if nX == nY:
            result = i
    return result

def solution1(X, Y, A):
    N = len(A)
    result = 0
    nX = 0
    nY = 0
    cur_len = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if nX == nY:
            cur_len += 1
            result = max(result, cur_len)
        else:
            cur_len = 0
    return result

def solution2(X, Y, A):
    N = len(A)
    result = -1
    nX = 0
    nY = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if nX == nY:
            if nX + nY == (i+1) // 2 + 1:
                result = i
    return result


A = [6,42,11,7,1,42]
X=7
Y=42 
print(solution(X, Y, A))
print(solution1(X, Y, A))
print(solution1(X, Y, A))
A = [6, 11, 7, 1, 42, 42]
X = 7
Y = 42
print(solution(X, Y, A))
print(solution1(X, Y, A))
print(solution2(X, Y, A))