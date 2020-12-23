from itertools import accumulate

def solve(nums):
    
    psum = [0] + list(accumulate(nums))    
    n = len(nums)
    ans = []
    for i in range(0, n):
        right = psum[n] - psum[i+1] - nums[i] * (n-i-1)
        left = nums[i] * i - psum[i]
        ans.append(left + right)
    
    return ans
        

if __name__ == "__main__":
    
    nums = [2,3,5]
    solve(nums)
    
    nums = [1,4,6,8,10]
    solve(nums)

