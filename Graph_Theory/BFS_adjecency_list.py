''' breadth first search using an adjacency list '''

def bfs(s):

    Graph = [''' adjecency list rep ''']

    visisted = [False]*len(Graph)
    queue = []

    queue.append(s)
    visisted[s] = True

    while queue:
        
        node = queue.pop(0)

        for i in Graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
        
