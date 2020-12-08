def solution(s, p):

    m, n = len(s), len(p)
    table = [[False] * (n+1) for i in range(m+1)]
    
    table[0][0] = True
    for j in range(1, n+1):
        table[0][j] = p[j-1] == '*' and table[0][j-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] != '*':
                table[i][j] = (p[j-1] == '?' or s[i-1] == p[j-1]) and table[i-1][j-1]
            else:
                case1 = table[i][j-1]           # match empty
                case2 = table[i-1][j]           # match one or more
                table[i][j] = case1 or case2
                
    return table[m][n]


if __name__ == "__main__":
    
    print(solution("aa", "?a"))
    print(solution("", "a"))
    print(solution("adceb", "*a*b"))
    print(solution("adcb", "a?b"))
    print(solution("aab", "c*a*b"))

