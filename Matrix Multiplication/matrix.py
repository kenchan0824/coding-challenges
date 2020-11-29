import sys

def matMulCost(A, i, j):
    
    if j <= i + 1:
        return 0
    
    minCost = sys.maxsize
    for k in range(i + 1, j):
        cost = A[i] * A[k] * A[j]
        cost += matMulCost(A, i, k)
        cost += matMulCost(A, k, j)
        if cost < minCost:
            minCost = cost
            
    return minCost


if __name__ == '__main__':
    
    A = [40, 20, 30, 10, 30]
    j = len(A) - 1
    print(matMulCost(A, 0, j))
    