t=int(input())
for i in range(t):
    s=input()
    dp=[0]*len(s)
    for i in range(len(s)):
        if s[i].isdigit()==False:
            dp[i]=1
    print(dp)
    if dp.count(0)==len(dp):
        print("Valid Format")
    elif dp.count(1)==len(dp):
        print("Its a String")
    else:
        print("Its an AlphaNumeric")
