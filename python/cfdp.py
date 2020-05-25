n=10**6
prime = [True for i in range(n+1)] 
p = 2
while (p * p <= n): 
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
dp=[0 for i in range(n+1)]
count=0
for i in range(2,n+1):
    if prime[i]==True:
        count+=1
    dp[i]=count
q=int(input())
for i in range(q):
    r1, r2=map(int,input().split())
    comp=(r1/r2)
    n=int(input())
    stri=input()
    stri="a"+stri
    dis=[float("inf")]*(n+1)
    if stri[1]=="*" or stri[n]=="*":
        print("No way!")
    else:
        dis[1]=0
        if 1+1<=n:
            if stri[2]!="*":
                dis[2]=min(dis[1]+1,dis[2])
        if 1+2<=n:
            if stri[3]!="*":
                dis[3]=min(dis[1]+1,dis[3])
        for i in range(2,n+1):
            if dis[i]!=float("inf"):
                if i+1<=n:
                    if stri[i+1]!="*":
                        dis[i+1]=min(dis[i]+1,dis[i+1])
                if i+2<=n:
                    if stri[i+2]!="*":
                        dis[i+2]=min(dis[i]+1,dis[i+2])
                if prime[i]==True:
                    if (dp[i]/i)>=comp:
                         if i+dp[i]<=n:
                             if stri[i+dp[i]]!="*":
                                 dis[i+dp[i]]=min(dis[i]+1,dis[i+dp[i]])
        if dis[n]==float("inf"):
            print("No way!")
        else:
            print(dis[n])
                    



