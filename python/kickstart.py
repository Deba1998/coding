from itertools import permutations
t=int(input())
for z in range(1,t+1):
    x, y=map(int,input().split())
    l=[[]for i in range(x)]
    for i in range(x):
        s=input()
        l[i]=list(s)
    xp=dict()
    for i in range(x):
        for j in range(y):
            if l[i][j] not in xp:
                xp[l[i][j]]=1
            else:
                xp[l[i][j]]+=1
    ws=""
    for i in xp:
        ws+=i
    li=permutations(ws)
    lip=[]
    for k in li:
        lip.append(''.join(k))
    for i in range(len(lip)):
        work=lip[i]
        dp=[[0 for i in range(y)]for i in range(x)]
        flag=0
        for aq in work:
            gem=0
            for i in range(y):
                if l[x-1][i]==aq:
                    dp[x-1][i]=1
            for i in range(x-2,-1,-1):
                cflag=0
                for j in range(y):
                    if l[i][j]==aq:
                        if dp[i+1][j]==1:
                            dp[i][j]=1
                        else:
                            gem=1
                            cflag=1
                            break
                if cflag==1:
                    break
            if gem==1:
                flag=1
                break
        if flag==0:
            break
    if flag==0:
        ans=work
    else:
        ans="-1"
    print("Case #"+str(z)+": "+ans)