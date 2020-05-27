n,m,k=map(int,input().split())
l=list(map(int,input().split()))
l=[0]+l
dp=[[]for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    dp[a].append([l[b],b])
    dp[b].append([l[a],a])
for i in range(1,n+1):
    if len(dp[i])<k:
        print(-1)
    else:
        dp[i].sort(reverse=True)
        print(dp[i][k-1][1])
for i in dp:
    print(i)