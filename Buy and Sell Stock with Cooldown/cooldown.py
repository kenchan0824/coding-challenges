def solution(prices):
    
    n = len(prices)
    if n <= 1: return 0
    
    stock = [0] * n             # balance with stock held at day i
    cash = [0] * n              # balance with cash held at day i
    
    # terminal condition
    stock[0] = -1 * prices[0]
    stock[1] = max(stock[0], -1 * prices[1])
    cash[1] = max(0, stock[0] + prices[1])
    
    for i in range(2, n):
        
        # dynamic programming recursion formula
        stock[i] = max(stock[i-1], cash[i-2] - prices[i])
        cash[i] = max(cash[i-1], stock[i-1] + prices[i])
    
    return cash[n-1]            # return last cash balance
    
    
if __name__ == '__main__':
    prices = [1,2,3,0,2]
    print(solution(prices))     # 3
