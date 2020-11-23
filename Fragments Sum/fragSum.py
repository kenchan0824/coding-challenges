"""
Write a function solution that, given an array A consisting of N integers, returns the 
number of fragments of A whoose sum equals 0 (that is, pairs (P,Q) such that P <= Q and 
the sum A[P] + A[P+1] + ... + A[Q] is 0). The function shuld return -1 if this number 
exceeds 1,000,000,000.

Examples:

1. Given A = [2, -2, 3, 0, 4, -7], the function should return 4, as explained on this
picture

2. Given A = [0, 0, ..., 0] of length 100,000, the function should return -1.

Write an efficient algorithm for the following assumptions:
    
    - N is an integer within the range [1 .. 100,0000];
    - each element of array A is an integer within the range [-10,000 .. 10,000].
"""

def solution(A):
    N = len(A)
    count = 0
    
    for i in range(0, N):
        cache = {}
        for j in range(i, N):
            if j == i:
                cache[j] = A[j]
                fragSum = A[j]
            else:
                fragSum = A[j] + cache[j-1]
                cache[j] = fragSum

            if fragSum == 0:
                count += 1
                
    return count
    

if __name__ == '__main__':
    
    A = [2, -2, 3, 0, 4, -7]
    print(solution(A))
