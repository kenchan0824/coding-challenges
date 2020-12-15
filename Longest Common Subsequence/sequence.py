def recursion(X, Y, m, n, mem={}):
    
    if m == 0 or n == 0:
        return 0
    
    if (m, n) in mem: return mem[(m, n)]
    
    if X[m-1] == Y[n-1]:
        mem[(m, n)] = 1 + recursion(X, Y, m-1, n-1)
        return mem[(m, n)]
    
    mem[(m, n)] = max(recursion(X, Y, m-1, n), recursion(X, Y, m, n-1))
    return mem[(m, n)]


def tabular(X, Y):
    
    m = len(X)
    n = len(Y)
    L = [[0] * (n+1) for i in range(0, m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):

            if X[i-1] == Y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]


if __name__ == '__main__':

    import string
    import random
    import time
    
    X = 'ABCBDAB'
    Y = 'BDCABA'
    
    A2Z = string.ascii_uppercase
    random.seed(1024)
    X = ''.join([(random.choice(A2Z)) for i in range(1000)])
    Y = ''.join([(random.choice(A2Z)) for i in range(1000)])
    
    start = time.time()
    #print(recursion(X, Y, len(X), len(Y)))
    print(tabular(X, Y))
    end = time.time()
    print('elapsed %.4f seconds' % (end - start))