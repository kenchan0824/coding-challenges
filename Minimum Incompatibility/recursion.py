from itertools import combinations

def solve(nums, size, dp = {}):
    if not nums: return 0
    if nums in dp: return dp[nums]
    
    ans = float('inf')
    for combo in combinations(set(nums), size):
        left = list(nums)
        for x in combo:
            left.remove(x)

        ans = min(ans, max(combo) - min(combo) + solve(tuple(left), size))
        dp[nums] = ans

    return ans

def minimumIncompatibility(nums, k):
    size = len(nums) // k
    result = solve(tuple(nums), size)
    return result if result != float('inf') else -1


if __name__ == "__main__":
    
    nums = [1,2,1,4]
    k = 2
    minimumIncompatibility(nums, k)

    nums = [5,3,3,6,3,3]
    k = 3
    minimumIncompatibility(nums, k)

    nums = [6,3,8,1,3,1,2,2]
    k = 4
    minimumIncompatibility(nums, k)
    
    nums = [6,8,5,16,8,12,11,7,13,16,15,14,7,9,1,10]
    k = 4
    minimumIncompatibility(nums, k)
    
    nums = [7,3,16,15,1,13,1,2,14,5,3,10,6,2,7,15]
    k = 8
    minimumIncompatibility(nums, k)
    