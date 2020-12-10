def solution(nums):

    n = len(nums)
    jumps, curr_far, last_dest = 0, 0, 0
    
    for i in range(0, n):
        if i > curr_far: return -1
        if i == n-1: return jumps
        curr_far = max(curr_far, i + nums[i])
        if i == last_dest:
            jumps += 1
            last_dest = curr_far
            
    return jumps


if __name__ == "__main__":
    
    nums = [2,2,1,0,4]
    print(solution(nums))

    nums = [1,3,1,0,4]
    print(solution(nums))

    nums = [0]
    print(solution(nums))
