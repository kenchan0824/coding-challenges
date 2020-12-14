from collections import defaultdict

def findOrder(numCourses, prerequisites):
    
    indegree = [0] * numCourses
    graph = defaultdict(list)
    for edge in prerequisites:
        indegree[edge[1]] += 1    
        graph[edge[0]].append(edge[1])
        
    startSet = []
    for c in range(numCourses):
        if indegree[c] == 0:
            startSet.append(c)
    
    stack = []
    while startSet:
        c = startSet.pop()
        stack.append(c)
        
        for t in graph[c]:
            indegree[t] -= 1
            if indegree[t] == 0:
                startSet.append(t)
                
    if startSet:
        stack.append(startSet)
    
    if max(indegree) > 0: return []
    return stack[::-1]
    

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
    
