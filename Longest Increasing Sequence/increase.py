def binary_search(L, longest, value):

    start = 0
    end = longest - 1
    while start <= end:
        mid = int((start + end) / 2)
        if L[mid] >= value:
            end = mid - 1
        else:            
            start = mid + 1
    
    return start

    
def solution(A):
    
    n = len(A)
    L = [None] * n

    L[0] = A[0]
    longest = 1

    for i in range(1, n):
        value = A[i]
        idx = binary_search(L, longest, value)
        L[idx] = value
        if idx == longest:
            longest += 1
            
    return longest

if __name__ == '__main__':
    
    A = [0, 3, 4, 5, 2, 7, 3, 4, 5, 6]
    print(solution(A))
