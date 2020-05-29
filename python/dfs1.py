def dfs(s,visited,level,parent):
    visited[s]=True
    res.append(s)
    level[s]=1
    for i in graph[s]:
        if visited[i]==False and i!=parent:
            dfs(i,visited,level,s)
            level[s]+=level[i]
n, q=map(int,input().split())
graph=[[] for i in range(n+1)]
l=list(input().split())
for i in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (len(graph))
level=[0]*len(graph)
res=[]
dfs(1,visited,level,0)
fuck=dict()
for i in range(len(res)):
    fuck[res[i]]=i
for j in range(q):
    bv, st=input().split()
    bv=int(bv)
    start=fuck[bv]
    tr=res[start:(start+level[bv])]
    stru=[]
    for i in tr:
        stru.append(l[i-1])
    x=dict()
    for i in stru:
        if i not in x:
            x[i]=1
        else:
            x[i]+=1
    y=dict()
    for j in st:
        if j not in y:
            y[j]=1
        else:
            y[j]+=1
    count=0
    for i in y:
        if i in x:
            count+=min(x[i],y[i])
    print(len(st)-count)
    

