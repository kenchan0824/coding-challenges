def solution(arr):
    
    n = len(arr)
    start, temp = 0, 0
    for i, num in enumerate(arr):
        if num > temp:
            start, temp = i, num
            
    jumps = 1
    queue = [start]
    while queue:
        size = len(queue)
        while size:
            i = queue.pop(0)
            size -= 1
            
            if start in [i + arr[i], i - arr[i]]: return jumps
            if arr[i] < 0: continue
            
            queue.append((i + arr[i]) % n)
            queue.append((i - arr[i]) % n)
            arr[i] = -arr[i]
        
        jumps += 1

    return -1


if __name__ == "__main__":

    arr = [2, 3, 5, 6, 1]    
    solution(arr)

    arr = [1, 2, 3, 4, 2]
    solution(arr)
    
    arr = [1, 7, 1, 1, 1, 1]
    solution(arr)
    
    arr = [0]
    solution(arr)
