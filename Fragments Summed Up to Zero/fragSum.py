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
