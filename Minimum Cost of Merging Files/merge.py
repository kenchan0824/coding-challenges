import time
import random

def greedy(A):

    cost = 0
    while len(A) > 1: 

        min1 = min(A)
        A.remove(min1)
        min2 = min(A)
        A.remove(min2)
        A.append(min1 + min2)
        cost += min1 + min2

    return cost


if __name__ == '__main__':
    
    #A = [100, 250, 1000]
    #A = [14, 25, 5, 8]
    A = [random.randrange(100) for i in range(10000)]

    start = time.time()

    print(greedy(A))

    end = time.time()
    print("--- %.4f seconds ---" % (end - start))