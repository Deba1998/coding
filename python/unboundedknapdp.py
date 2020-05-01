#bottom up
def knap(n,w,val,weight):
    dp=[[0 for i in range(w+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif weight[i-1]<=j:
                dp[i][j]=max(val[i-1]+dp[i][j-weight[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return(dp[n][w])
val=[60,100,120]
l=[10,20,30]
print(knap(3,50,val,l))
'''#top down
def knap(n,w,val,weight):
    if dp[n][w]!=-1:
        return(dp[n][w])
    else:
        if n==0 or w==0:
            dp[n][w]=0
        elif weight[n-1]<=w:
            dp[n][w]=max((val[n-1]+knap(n,w-weight[n-1],val,weight)),knap(n-1,w,val,weight))
        else:
            dp[n][w]=knap(n-1,w,val,weight)
        return(dp[n][w])
val=[60,100,120]
l=[10,20,30]
dp=[[-1 for i in range(50+1)]for i in range(3+1)]
print(knap(3,50,val,l))'''