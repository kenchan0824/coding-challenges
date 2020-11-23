def longestCommonSequence(X, Y, m, n):
    
    if m == 0 or n == 0:
        return 0
    
    if X[m-1] == Y[n-1]:
        return 1 + longestCommonSequence(X, Y, m-1, n-1)
    
    return max(longestCommonSequence(X, Y, m-1, n), longestCommonSequence(X, Y, m, n-1))


if __name__ == '__main__':

    X = 'ABCBDAB'
    Y = 'BDCABA'
    print(longestCommonSequence(X, Y, len(X), len(Y)))
    