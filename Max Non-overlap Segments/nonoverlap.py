def greedy(A, B):
    
    count = 1
    n = len(B)
    end = B[0]
    for i in range(1, n):
        if A[i] > end:
            count += 1
            end = B[i]            

    return count


if __name__ == '__main__':
    
    A = [1, 3, 7, 9, 9]
    B = [5, 6, 8, 9, 10]
    
    greedy(A, B)
