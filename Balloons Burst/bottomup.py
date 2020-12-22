def solution(nums):
    
    n = len(nums)
    nums = [1] + nums + [1]
    table = [[0] * (n+2) for _ in range(n+2)]
    
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            for k in range(i, j+1):
                table[i][j] = max(table[i][j],
                        table[i][k-1] + table[k+1][j] +
                        nums[i-1] * nums[k] * nums[j+1])
                
    return table[1][n]

nums = [3,1,5,8]
solution(nums)
