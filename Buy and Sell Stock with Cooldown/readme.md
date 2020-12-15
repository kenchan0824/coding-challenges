Buy and Sell Stock with Cooldown
===



Say you have an array for which the `i`th element is the price of a given stock on day `i`.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (i.e., cooldown 1 day)



**Example:**

Input: 
```
[1,2,3,0,2]
```
Output: 
```
3 
```
Explanation: 
```
transactions = [buy, sell, cooldown, buy, sell]
```



#dynamic-programming 	#O(n)