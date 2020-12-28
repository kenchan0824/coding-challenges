from heapq import heappush, heappop

def solution(apples, days):
    heap = []
    n = len(apples)
    d = eat = 0
    while d < n or heap:
        while heap and heap[0][0] <= d:
            heappop(heap)
        if d < n and apples[d] > 0:
            heappush(heap, [d+days[d], apples[d]])
        if heap:
            eat += 1
            heap[0][1] -= 1
            if heap[0][1] == 0: heappop(heap)
        d += 1
    
    return eat

if __name__ == "__main__":
    
    apples = [1,2,3,5,2]
    days = [3,2,1,4,2]
    solution(apples, days)
    apples = [3,0,0,0,0,2]
    days = [3,0,0,0,0,2]
    solution(apples, days)