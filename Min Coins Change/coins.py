import sys

def minCoins(coins, m, n, dp={}):
    
    if n == 0:
        return 0
    
    if n < 0:
        return sys.maxsize
    
    if m == 0 and n > 0:
        return sys.maxsize
      
    if (m,n) in dp:
        return dp[(m,n)]
    
    dp[(m,n)] = min(minCoins(coins, m-1, n), 1 + minCoins(coins, m, n - coins[m-1]))

    return dp[(m,n)]


if __name__ == '__main__':

#    coins = [1, 3, 4]
#    n = 6
    coins = [9, 6, 5, 1]
    n = 11
    print(minCoins(coins, len(coins), n))