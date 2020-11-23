import time
import numpy as np

def solution(A):
    N = 100000
    A = set(A)
    for t in range(1, N):
        if t not in A:
            return(t)

    return N


if __name__ == '__main__':  
    
    #A = [1, 3, 6, 4, 1, 2]
    A = np.arange(1, 100000)
    np.random.shuffle(A)
    
    start_time = time.time()
    print(solution(A))
    print("--- %s seconds ---" % (time.time() - start_time))
    
