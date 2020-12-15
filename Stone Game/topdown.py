def firstWin(piles):
    n = len(piles)
    dp = [[0] * n for _ in range(n)]
    
    def solve(i, j):
        if i > j: return 0
        if dp[i][j] != 0: return dp[i][j]
        
        diff = piles[i] - solve(i+1, j)
        diff = max(diff, piles[j] - solve(i, j-1))
        dp[i][j] = diff
        return diff        

    return solve(0, n-1) > 0

piles = [5,3,4,5]
firstWin(piles)