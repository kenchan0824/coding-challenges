def solution(prices):
    
    n = len(prices)
    stock = cash = 0
    stock = -1 * prices[0]
    
    for i in range(1, n):
        stock = max(stock, - prices[i])         # balance with stock held
        cash = max(cash, stock + prices[i])     # balance with all cash

    return cash


if __name__ == '__main__':
    
    prices = [7,1,5,3,6,4]
    print(solution(prices))                     # 5
    