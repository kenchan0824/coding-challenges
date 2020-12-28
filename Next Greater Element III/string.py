def solution(num):
    num = list(str(num))
    i = j = len(num) - 1
    while i > 0:
        if num[i-1] < num[i]: break
        i -= 1
    
    if i == 0: return -1
    
    while j < len(num) and j >= i:
        if num[j] > num[i-1]: break
        j -= 1
    
    num[i-1], num[j] = num[j], num[i-1]
    ans = int("".join(num[:i] + num[i:][::-1]))
    return ans if ans <= 2**31 else -1

num = 1234765553
solution(num)
num = 765553
solution(num)
num = 1999999999
solution(num)
