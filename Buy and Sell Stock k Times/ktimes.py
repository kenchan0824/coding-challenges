def solution(prices, k):
    
    if k == 0: return 0
    
    n = len(prices)
    if n == 0: return 0
    
    stock = [-1 * prices[0]] * k
    cash = [0] * k
    
    for i in range(1, n):
        stock[0] = max(stock[0], -1 * prices[i]) 
        cash[0] = max(cash[0], stock[0] + prices[i])
        for j in range(1, k):
            stock[j] = max(stock[j], cash[j-1] - prices[i]) 
            cash[j] = max(cash[j], stock[j] + prices[i])

    return cash[k-1]


if __name__ == '__main__':
    
    prices = [3,3,5,0,0,3,1,4]
    k = 2
    print(solution(prices, k))                         # 6
    