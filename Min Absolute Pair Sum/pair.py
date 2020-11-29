def solution(A):
    # write your code in Python 3.6
    A =sorted(A)
    back = 0
    front = len(A) - 1
    
    min_sum = 2000000000
    while(front >= back):
        min_sum = min(min_sum, abs(A[front] + A[back]))
        if min_sum == 0: break
        
        if abs(A[front]) > abs(A[back]):
            front -= 1
        else:
            back += 1

    return min_sum


if __name__ == '__main__':

    import time
    import random

    #A = [-8, 4, 5, -10, 3]
    A = [random.randint(-1000000000, 1000000000) for i in range(0, 100000)]
    
    start = time.time()
    print(solution(A))
    end = time.time()
    print('elapsed %.4f seconds.' % (end - start))
    
