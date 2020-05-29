def BFS(s,visited,level): 
    queue = []        
    queue.append(s) 
    visited[s] = True
    while queue: 
        s = queue.pop(0) 
        for i in graph[s]: 
            if visited[i] == False: 
                level[i]=level[s]+1
                queue.append(i) 
                visited[i] = True
    return(level)
n,m=map(int,input().split())
graph=[[]for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(int(input())):
    u,v=map(int,input().split())
    visited = [False] * (len(graph))
    level=[0]*len(graph)
    ws=BFS(u,visited,level)
    count=0
    for i in ws:
        if i==v:
            count+=1
    print(count)
