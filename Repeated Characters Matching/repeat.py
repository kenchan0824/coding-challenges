def allmatch(s, start, num):

    if start < 0: return False
    if len(s) < start + num: return False
    for i in range(num-1):
        if not s[start+i] == s[start+i+1]: return False
    return True


def solution(s, p):

    m, n = len(s), len(p)
    table = [[False] * (n+1) for _ in range(m+1)]
    numeric = [str(x) for x in range(1,10)]
    alphabetic = [chr(x) for x in range(ord('a'), ord('z')+1)]
    
    table[0][0] = True
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '$':
                table[i][j] = s[i-1] in numeric and table[i-1][j-1]
            elif p[j-1] == '+':
                table[i][j] = s[i-1] in alphabetic and table[i-1][j-1]
            elif p[j-1] == '*':
                if j > n-1 or p[j] != '{':
                    table[i][j] = allmatch(s, i-3, 3) and table[i-3][j-1]
                else:
                    close = p.find('}', j)
                    if close == -1: return False
                    k = int(p[j+1:close])
                    table[i][close+1] = allmatch(s, i-k, k) and table[i-k][j-1]
                
    return table[m][n]

    
if __name__ == "__main__":
    
    testcase = { 
            ("9", "$"): True,
            ("a", "$"): False,
            ("99", "$"): False,
            ("", "$"): False,
            ("9", "$$"): False,
            ("z", "+"): True,
            ("z1", "+$"): True,
            ("1", "+"): False,
            ("222", "*"): True,
            ("33", "*"): False,
            ("444", "*", ): True,
            ("", "*"): False,
            ("aaaa", "+*"): True,
            ("aa", "*{2}"): True,
            ("abcdehhhhhh", "+++++*"): False,
            ("abcdehhh", "+++++*"): True,
            ("9mmmrrrkbbb", "$**+*{2}"): False,
            ("9mmmrrrkbb", "$**+*{2}"): True,
            ("1111111111", "*{10}"): True,
            ("111111111", "*{10}"): False,
            }

    for key in testcase:
        output = solution(*key)
        if output != testcase[key]:
            print('Intput: %s, Expect: %s, Output: %s' % 
                  (key, testcase[key], output))
    
    print('Done')
