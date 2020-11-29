def solution(A):
    
    total = running = 0
    n = len(A)
    for i in range(1, n):
        running = max(0, running + A[i] - A[i-1])
        total = max(total, running)

    return total

if __name__ == '__main__':
    
    A = [23171, 21011, 21123, 21366, 21013, 21367]
    print(solution(A))