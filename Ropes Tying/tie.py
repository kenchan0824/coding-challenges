def solution(K, A):
    count = 0
    rope = 0
    n = len(A)
    for i in range(0, n):
        
        if A[i] + rope >= K:
            count +=1
            rope = 0
        else:
            rope += A[i]

    return count


if __name__ == '__main__':
    
    A = [1, 2, 3, 4, 1, 1, 3]
    K = 4
    solution(K, A)
