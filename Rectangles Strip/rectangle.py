# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):

    C = {}
    N = len(A)
    for i in range(N):
        a = A[i] 
        if a not in  C:
            C[a] = 1
        else:
            C[a] += 1
        
        b = B[i]
        if b == a: continue
        if b not in  C:
            C[b] = 1
        else:
            C[b] += 1
        
        
    max_ = 0
    for k, v in C.items():
        if v > max_: max_ = v

    return max_


if __name__ == '__main__':
     A = [2, 10, 4, 1, 4]
     B = [4, 1, 2, 2, 5]
     #A = [2, 3, 1, 3]
     #B = [2, 3, 1, 3]
     A = [2, 3, 2, 3, 5]
     B = [3, 4, 2, 4, 2]
     print(solution(A, B))

