import time
import random


def solution(A):
    N = len(A)
    V = 0
    for i in range(1, N-1):
        left = max(A[:i])        
        right = max(A[i+1:])
        L = min(left, right)
        V += max(L - A[i], 0)
        
    return V


def solution_fast(A):
    N = len(A)
    right = [None] * N
    right[N-1] = A[N-1]
    for i in range(N-2, 0, -1):
        right[i] = max(right[i+1], A[i+1])

    V = 0
    left = A[0]
    for i in range(1, N-1):
        left = max(left, A[i-1])
        level = min(left, right[i])
        V += max(level - A[i], 0)
        
    return V


if __name__ == '__main__':
    
    start = time.time()

    #A = [0, 1, 4, 0, 0, 2, 0, 3, 1, 0]
    A = [random.randint(0, 10) for i in range(0, 1000000)]
    print(solution_fast(A))

    print("elapsed %.4f seconds.\n" % (time.time() - start))