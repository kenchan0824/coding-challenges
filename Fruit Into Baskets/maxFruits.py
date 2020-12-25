from collections import defaultdict

def maxfruits(tree):

    n = len(tree)
    k = 2
    fruits = i = 0
    table = defaultdict(int)
    for j in range(n):
        
        if table[tree[j]] == 0: k -= 1
        table[tree[j]] += 1
    
        while k < 0:
            table[tree[i]] -= 1
            if table[tree[i]] == 0: k += 1
            i += 1
    
        fruits = max(fruits, j - i + 1)
    
    return fruits


if __name__ == "__main__":
    
    tree = [3,3,3,1,2,1,1,2,3,3,4]
    maxfruits(tree)
