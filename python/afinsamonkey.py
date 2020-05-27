k,a,b=map(int,input().split())
s=input()
lent=len(s)
if lent>(k*b) or lent<(k*a):
    print("No solution")
else:
    dp=[a]*k
    rem=lent-(sum(dp))
    i=0
    while rem>0:
        dp[i]+=1
        i=(i+1)%k
        rem-=1
    pref=[0]*(k+1)
    pref[1]=dp[0]
    for i in range(1,k+1):
        pref[i]=pref[i-1]+dp[i-1]
    for i in range(1,k+1):
        print(s[pref[i-1]:pref[i]])


