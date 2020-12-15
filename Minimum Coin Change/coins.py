import sys
import time

def recursion(coins, value, mem = {}):
    
    if value == 0: return 0
    
    if value in mem: return mem[value]
    
    result = sys.maxsize
    for coin in coins:
        if coin > value: continue
    
        remain = value - coin
        result = min(result, 1 + recursion(coins, remain))

    mem[value] = result
    return result


def tabular(coins, value):
    
    table = [sys.maxsize] * (value+1)
    table[0] = 0
    
    for v in range(1, value+1):
        
        for coin in coins:
            if coin > v: continue
            remain = v - coin
            table[v] = min(table[v], 1 + table[remain])
            
    return table[value] if table[value] != sys.maxsize else -1
    

if __name__ == '__main__':

    #coins = [3, 4]
    #value = 5
    coins = [1, 5, 6, 9]
    #value = 11
    value = 100000
    
    start = time.time()
    #print(recursion(coins, value))
    print(tabular(coins, value))
    end = time.time()
    print('elapsed %.4f seconds' % (end - start))