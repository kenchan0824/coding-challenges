from bisect import bisect_left

def solution(A):
    
    L = [None] * len(A)
    longest = 0
    for a in A:
        idx = bisect_left(L, a, 0, longest)
        L[idx] = a
        if idx == longest:
            longest += 1
            
    return longest

if __name__ == '__main__':
    
    A = [0, 3, 4, 5, 2, 7, 3, 4, 5, 6]
    print(solution(A))
