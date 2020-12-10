def solution(arr, start):
    
    n = len(arr)
    queue = [start]    

    while queue:
        
        i = queue.pop(0)
        if arr[i] == 0: return True
        if arr[i] < 0: continue
                
        if i - arr[i] >= 0:
            queue.append(i - arr[i])
        if i + arr[i] < n:
            queue.append(i + arr[i])

        arr[i] = -arr[i]
        
    return False
    
arr = [4,2,3,0,3,1,2]
start = 0
solution(arr, start)

arr = [3,0,2,1,2]
start = 2
solution(arr, start)
