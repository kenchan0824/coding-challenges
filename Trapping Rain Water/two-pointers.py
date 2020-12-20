def solution(height):
    right = len(height) -1
    left = left_max = right_max = water = 0
    while left <= right:
        
        if left_max < right_max:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
            
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
            
    return water


if __name__ == "__main__":
        
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    soultion(height)
    
    height = [4,2,0,3,2,5]
    soultion(height)
    