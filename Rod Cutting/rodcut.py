def rodCut(price, n):

    if n == 1:
        return price[0]
    
    maxProfit = 0
    for k in range(0, n):
        profit = price[k] + rodCut(price, n-k-1)
        if profit > maxProfit:
            maxProfit = profit
            
    return maxProfit


if __name__ == '__main__':

    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(rodCut(price, 4))
