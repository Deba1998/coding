'''def KnapSack(val, wt, n, W): 
    dp = [0]*(val+1) 
    for i in range(n): 
        for j in range(0,val[i]): 
            dp[j]=min(dp[j],wt[i]+dp[j-val[i]])
n,c=map(int,input().split())
value=list(map(int,input().split()))
weight=list(map(int,input().split()))
print(KnapSack(value,weight,n,c))'''
def KnapSack():
    for i in range(n+1):
        for j in range(50000,0,-1):
            if j==0:
                dp[j]=0
            elif i==0:
                dp[j]=float("inf")
            elif j>=val[i-1]:
                dp[j]=min(dp[j],dp[j-val[i-1]]+cost[i-1])
            else:
                dp[j]=dp[j]
    m=0
    for j in range(50001):
        if dp[j]<=c:
            m=j
    return(m)
n,c=map(int,input().split())
val=list(map(int,input().split()))
cost=list(map(int,input().split()))
dp=[0]*(50005)
print(KnapSack())    
