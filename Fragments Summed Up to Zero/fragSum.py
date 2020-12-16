from collections import defaultdict

def solution(A):
    table = defaultdict(int)
    table[0] = 1    
    count, psum = 0, 0
    for a in A:
        psum += a
        count += table[psum]
        table[psum] += 1
                
    return count

if __name__ == '__main__':
    
    from random import randint
    import time
    
#    A = [2, -2, 3, 0, 4, -7]
    A = [randint(-100, 100) for _ in range(100000)]
    start = time.time()
    print(solution(A))
    end = time.time()
    print("elapsed %.4f seconds" % (end - start))
    
