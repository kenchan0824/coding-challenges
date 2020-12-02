import random
import time

def recursion(P, n, mem={}):

    if n == 1:
        return P[0]
    
    if n in mem: return mem[n]
    
    maxProfit = 0
    for k in range(0, n):
        remain = n - (k + 1)
        profit = P[k] + recursion(P, remain, mem)
        maxProfit = max(maxProfit, profit)
            
    mem[n] = maxProfit
    return maxProfit


def tabular(P, n):
    
    table = [0] * (n + 1)
    
    for l in range(1, n+1):
        for k in range(0, l):
            remain = l - (k + 1)
            table[l] = max(table[l], P[k] + table[remain])

    return table[n]


if __name__ == '__main__':

#    P = [1, 5, 8, 9]
#    n = 4
    n = 1000
    P = sorted([random.randint(1, 10000) for i in range(n)])
    
    start = time.time()
#    print(recursion(P, n, {}))
    print(tabular(P, n))
    end = time.time()
    print('elapsed %.4f seconds.' % (end - start))