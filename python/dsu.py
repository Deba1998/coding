
def find(a):
	if par[a]==a:
		return a
	else:
		par[a]=find(par[a])
		return par[a]
def union(a,b):
	a,b=find(a),find(b)
	if a!=b:
		if rank[a]>rank[b]:
			par[b]=a
		elif rank[b]>rank[a]:
			par[a]=b
		else:
			par[a]=b
			rank[b]+=1


n,m=map(int,input().split())
par=[i for i in range(n+1)]
rank=[0 for i in range(n+1)]
cost=[-1 for i in range(n+1)]
for i in range(m):
	u, v=map(int,input().split())
	union(u,v)

up=set()

for i in range(1,(n+1)):
	c=int(input())
	up.add(find(i))
	if c>=0:
		if cost[find(i)]==-1:
			cost[find(i)]=c
		else:
			cost[find(i)]=min(cost[find(i)],c)
if len(up)==1:
	print(0)
else:
	flag=True
	for i in up:
		if cost[i]==-1:
			print(-1);flag=False
			break
	if flag:
		t1=[cost[x] for x in up];t1.sort()
		#print(t1)
		print(sum(t1)+(len(t1)-2)*t1[0])