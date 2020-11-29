Given a value V and array coins[] of size n, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins[1], coins[2], ..., coins[n]} valued coins. Find the minimum number of coins to make the change. If not possible to make change then output -1

Example 1:
Input: V = 30, n = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin and one 5 cent coin

Example 2:
Input: V = 11, n = 4, coins[] = {9, 6, 5, 1} 
Output: 2 
Explanation: Use one 6 cent coinand one 5 cent coin

Your Task:  
Complete the function minCoins() which takes V, n and array coins as input parameters and returns the answer.

Expected Time Complexity: O(V x n)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V x n ≤ 106
All the elements of array are distinct