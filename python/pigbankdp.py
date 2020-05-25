#bottom up
def knap(n,w,val,weight):
    dp=[[0 for i in range(w+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                dp[i][j]=0
            if i==0:
                dp[i][j]=float("inf")
            if i==1:
                if j%weight[i-1]==0:
                    dp[i][j]=val[i-1]*(j//weight[i-1])
                else:
                    dp[i][j]=float("inf")
            elif weight[i-1]<=j:
                dp[i][j]=min(val[i-1]+dp[i][j-weight[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return(dp[n][w])
for i in range(int(input())):
    e , f=map(int,input().split())
    we=(f-e)
    value=[]
    wei=[]
    n=int(input())
    for i in range(n):
        x, y=map(int,input().split())
        value.append(x)
        wei.append(y)
    ans=knap(n,we,value,wei)
    if ans==float("inf"):
        print("This is impossible.")
    else:
        print("The minimum amount of money in the piggy-bank is "+str(ans)+".")
