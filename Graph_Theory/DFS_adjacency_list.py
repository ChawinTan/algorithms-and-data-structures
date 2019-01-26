Graph = [''' adecency list rep ''']
visited = [False]*len(Graph)

def bfs(s, visited):
    
    visited[s] = True

    for i in Graph[s]:
        if visisted[i] == False:
            bfs(i, visited)
        

''' to detect a cycle in a grapsh,
    use another variable called recStack.

    If the node is in the recursion and
    is visited, then it is cyclic
'''
