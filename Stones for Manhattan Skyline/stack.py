def solution(H):
    block = 0
    stack = []
    for h in H:
        
        while stack and h < stack[-1]:
            stack.pop()
            block += 1
    
        if not stack or h != stack[-1]:
            stack.append(h)
    
    return block + len(stack)


if __name__ == "__main__":

    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    solution(H)
    