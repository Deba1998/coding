def BFS(s,visited): 
    queue = []        
    queue.append(s) 
    visited[s] = True
    while queue: 
        s = queue.pop(0) 
        print (s, end = " ") 
        for i in graph[s]: 
            if visited[i] == False: 
                queue.append(i) 
                visited[i] = True

graph=[[1,2],[0,3],[0,4],[1],[2]]
visited = [False] * (len(graph))
BFS(0,visited) 