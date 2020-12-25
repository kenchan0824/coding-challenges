def solution(A, B):
    n=len(A)
    stack = []
    fish = 0
    for i in range(n):
        
        if B[i] == 0:
            while stack and stack[-1] < A[i]:
                stack.pop()
            if not stack: fish +=1
        else:
            stack.append(A[i])
    
    return fish + len(stack)


if __name__ == "__main__":
    
    A = [4,3,2,1,5]
    B = [0,1,0,0,0]
    solution(A, B)
