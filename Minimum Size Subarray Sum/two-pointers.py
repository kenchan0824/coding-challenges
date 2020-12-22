def minSubArrayLen(nums, s):
    n = len(nums)
    sum = slow = 0
    ans = float('inf')
    for fast in range(n):
        sum += nums[fast]
    
        while sum >= s:
            ans = min(ans, fast - slow + 1)
            sum -= nums[slow]
            slow += 1

    return ans if ans != float('inf') else 0


if __name__ == "__main__":
    
    nums = [2,3,1,2,4,3]
    s = 7
    minSubArrayLen(nums, s)
    
    nums = [1,1]
    s = 3
    minSubArrayLen(nums, s)
