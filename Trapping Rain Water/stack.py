def soultion(height):
        
    water = 0
    stack = []
    for j, y in enumerate(height):
        while stack and y > stack[-1][1]:
            _, bottom = stack.pop()
            if stack:
                i, x = stack[-1]
                water += (j-i-1) * (min(x, y) - bottom)
        
        stack.append((j, y))

    return water


if __name__ == "__main__":
        
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    soultion(height)
    
    height = [4,2,0,3,2,5]
    soultion(height)
    