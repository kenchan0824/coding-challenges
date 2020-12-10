def solution(nums):
    
    coverage = 0
    n = len(nums)
    for i in range(n):
        if i > coverage: return False
        coverage = max(coverage, i + nums[i])
        if coverage >= n-1: return True
        
    return False

if __name__ == "__main__":
    
    nums = [2,3,1,1,4]
    solution(nums)

    nums = [3,2,1,0,4]
    solution(nums)
