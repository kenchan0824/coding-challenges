def solve(nums, k):

    n = len(nums)
    stack = []
    for i, num in enumerate(nums):
        while stack and num < stack[-1] and n-i > k-len(stack):
            stack.pop() 
        if len(stack) < k:
            stack.append(num)
            
    return stack
                
if __name__ == "__main__":
        
    nums = [3,5,2,6]
    k = 2
    solve(nums, k)
    
    nums = [2,4,3,3,5,4,9,6]
    k = 4
    solve(nums, k)
    
    nums = [71,18,52,29,55,73,24,42,66,8,80,2]
    k = 3
    solve(nums, k)
