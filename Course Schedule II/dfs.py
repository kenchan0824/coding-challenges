from collections import defaultdict

def dfs(node, edges, stack, visit, cycle):
    if visit[node]: return True
    visit[node] = True
    cycle[node] = True
    
    for child in edges[node]:
        if cycle[child]: return False
        if visit[child]: continue
    
        if not dfs(child, edges, stack, visit, cycle): return False
    
    cycle[node] = False
    stack.append(node)
    return True

def findOrder(numCourses, prerequisites):
    
    edges = defaultdict(list)
    for pair in prerequisites:
        edges[pair[0]].append(pair[1])

    stack = []
    visit = [False] * numCourses
    cycle = [False] * numCourses
    for root in range(numCourses):
        if visit[root]: continue
        if not dfs(root, edges, stack, visit, cycle): return []
    
    return stack


if __name__ == "__main__":
    
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    findOrder(numCourses, prerequisites)
    
    numCourses = 2
    prerequisites = [[0,1],[1,0]]
    findOrder(numCourses, prerequisites)
    
    numCourses = 2
    prerequisites = [[0,1]]
    findOrder(numCourses, prerequisites)
    
    numCourses = 3
    prerequisites = [[0,1],[0,2],[1,2]]
    findOrder(numCourses, prerequisites)
    
