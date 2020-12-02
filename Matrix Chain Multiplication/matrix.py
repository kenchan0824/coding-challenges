import sys
import time
import random

def recursion(A, i, j, mem = {}):
    
    if j == i + 1: return 0
    
    if (i, j) in mem: return mem[(i, j)]
    
    minCost = sys.maxsize
    for k in range(i + 1, j):
        cost = A[i] * A[k] * A[j]
        cost += recursion(A, i, k)
        cost += recursion(A, k, j)
        minCost = min(minCost, cost)

    mem[(i, j)] = minCost
    return minCost


def tabular(A):
    
    n = len(A)
    table = [[sys.maxsize] * n for i in range(n)]

    # single matrix
    for i in range(0, n-1):
        table[i][i+1] = 0

    # subproblems with 2 to n-1 matrices
    for l in range(2, n):
        for i in range(0, n-l):
            j = i + l
            for k in range(i + 1, j):
                cost = A[i] * A[k] * A[j]
                cost += table[i][k]
                cost += table[k][j]
                table[i][j] = min(table[i][j], cost)

    return table[0][n-1]

            
if __name__ == '__main__':
    
#    A = [40, 20, 30, 10, 30]
    A = [random.randint(1, 100) for i in range(100)]

    start = time.time()
#    print(recursion(A, 0, len(A) - 1))
    print(tabular(A))
    end = time.time()
    print('elapsed %.4f seconds' % (end - start))