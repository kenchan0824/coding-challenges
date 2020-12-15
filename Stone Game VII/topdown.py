from itertools import accumulate

def solution(stones):

    psum = [0] + list(accumulate(stones))
    n = len(stones)
    table = [[None] * n for _ in range(n)]

    def solve(i, j):
        
        if i == j: 
            return 0
        
        if table[i][j]: return table[i][j]
        
        case1 = psum[j+1] - psum[i+1] - solve(i+1, j)
        case2 = psum[j] - psum[i] - solve(i, j-1)
        table[i][j] = max(case1, case2)
    
        return table[i][j]

    return solve(0, n-1)

if __name__ == "__main__":
    
    stones = [5,3,1,4,2]
    solution(stones)

    stones = [1,1,1,1,1,1,1,7,7,1,1,1,1,1,1,1]
    solution(stones)

