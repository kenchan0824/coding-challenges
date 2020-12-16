from heapq import heapify, heappush, heappop

def greedy(A):

    heapify(A)
    
    cost = 0
    while len(A) > 1: 

        min1 = heappop(A)
        min2 = heappop(A)
        cost += min1 + min2
        heappush(A, min1 + min2)

    return cost


if __name__ == '__main__':
    
    import time
    import random

    #A = [100, 250, 1000]
    #A = [14, 25, 5, 8]
    A = [random.randrange(100) for i in range(100000)]

    start = time.time()

    print(greedy(A))

    end = time.time()
    print("--- %.4f seconds ---" % (end - start))