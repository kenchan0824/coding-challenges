from itertools import accumulate

def maximumUniqueSubarray(nums):

    psum = [0] + list(accumulate(nums))
    queue = set()
    score = i = 0
    n = len(nums)
    for j in range(n):
        while nums[j] in queue:
            queue.remove(nums[i])
            i += 1

        score = max(score, psum[j+1] - psum[i])
        queue.add(nums[j])

    return score

if __name__ == "__main__":
    
    nums = [4,2,4,5,6]
    maximumUniqueSubarray(nums)

    nums = [5,2,1,2,5,2,1,2,5]
    maximumUniqueSubarray(nums)
