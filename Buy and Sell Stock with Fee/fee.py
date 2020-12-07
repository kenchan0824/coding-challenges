def solution(prices, fee):
    
    n = len(prices)
    if n == 0: return 0
    
    stock = cash = 0
    stock = -1 * prices[0] - fee
    
    for i in range(1, n):
        stock = max(stock, cash - prices[i] - fee)      # balance with stock held
        cash = max(cash, stock + prices[i])             # balance with all cash

    return cash


if __name__ == '__main__':
    
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(solution(prices, fee))                             # 8
    