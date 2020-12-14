from collections import defaultdict

def canFinish(numCourses, prerequisites):

    graph = defaultdict(list)
    for edge in prerequisites:
        graph[edge[0]].append(edge[1])
    
    def cyclic(root, stack, visit):
        
        if root in stack: return True
        
        stack.add(root)
        for child in graph[root]:
            if child in visit: continue
            if cyclic(child, stack, visit): return True
    
        stack.pop()
        visit.add(root)
        return False

    visit = set()
    for node in range(numCourses):
        if cyclic(node, set(), visit): return False

    return True

if __name__ == "__main__":
    
    numCourses = 2
    prerequisites = [[1,0]]
    canFinish(numCourses, prerequisites)
    
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    canFinish(numCourses, prerequisites)

