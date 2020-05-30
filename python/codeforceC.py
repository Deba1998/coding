def KnapSack(val, wt, n, W): 
    dp = [0]*(W+1) 
    for i in range(n): 
        for j in range(W,wt[i]-1,-1): 
            dp[j]=max(dp[j],val[i]+dp[j-wt[i]]) 
    return dp[W] 
n,c=map(int,input().split())
value=list(map(int,input().split()))
weight=list(map(int,input().split()))
print(KnapSack(value,weight,n,c))