def solution(prices):
    
    n = len(prices)
    stock1 = cash1 = stock2 = cash2 = 0
    stock1 = stock2 = -1 * prices[0]                # day 1 balance with stock held
    
    for i in range(1, n):
        stock1 = max(stock1, - prices[i])           # balance with stock held 1st time
        cash1 = max(cash1, stock1 + prices[i])      # balance with all cash 1st time
        stock2 = max(stock2, cash1 - prices[i])     # balance with stock held 2nd time
        cash2 = max(cash2, stock2 + prices[i])      # balance with all cash 2nd time

    return cash2


if __name__ == '__main__':
    
    prices = [3,3,5,0,0,3,1,4]
    print(solution(prices))                         # 4
    