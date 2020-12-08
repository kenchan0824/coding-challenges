def solution(s, p):
    
    m, n = len(s), len(p)
    table = [[False] * (n+1) for i in range(m+1)]
    
    table[0][0] = True
    for j in range(2, n+1):
        table[0][j] = p[j-1] == '*' and table[0][j-2]
    
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] != '*':
                table[i][j] = (p[j-1] == '.' or s[i-1] == p[j-1]) and table[i-1][j-1]
            else:
                if j < 2: continue
                case1 = table[i][j-2]                                           # empty
                case2 = (p[j-2] == '.' or s[i-1] == p[j-2]) and table[i-1][j]   # many
                table[i][j] = case1 or case2
                
    return table[m][n]
                

if __name__ == '__main__':
    s = "aab"
    p = "c*a*b"
    print(solution(s, p))
