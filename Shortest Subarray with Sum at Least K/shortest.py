from itertools import accumulate
from collections import deque

def solution(A, K):
    psum = [0] + list(accumulate(A))
    
    ans = float('inf')
    monoq = deque()
    for y, py in enumerate(psum):

        while monoq and py - psum[monoq[0]] >= K:
            ans = min(ans, y - monoq.popleft())

        while monoq and psum[monoq[-1]] >= py: 
            monoq.pop()
    
        monoq.append(y)
            
    return ans if ans != float('inf') else -1
    

if __name__ == "__main__":
        
    A = [2,-1,2]
    K = 3
    solution(A, K)
    
    A = [77,19,35,10,-14]
    K = 19
    solution(A, K)

    A = [-5, -8]
    K = -6
    solution(A, K)
