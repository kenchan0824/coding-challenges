def solution(nums):

    def solve(nums, i, j):
    
        if i > j: return 0
        
        coin = 0
        for k in range(i, j+1):
            coin = max(coin, solve(nums, i, k-1) + solve(nums, k+1, j) + 
                       nums[i-1] * nums[k] * nums[j+1])
    
        return coin

    nums = [1] + nums + [1]
    n = len(nums)
    return solve(nums, 1, n-2)

nums = [3,1,5,8]
solution(nums)
