s1,s2=input().split()
n=len(s1)
m=len(s2)
if m==n:
    flag=0
    for i in range(0,m):
        gh=s2[i:]+s2[:i]
        if gh==s1:
            flag=1
            break
    if flag==1:
        print("true")
    else:
        print("false")
else:
    for i in range(m-n+1):
        pi=s2[i:(i+n)]
        flag=0
        for i in range(0,n):
            gh=pi[i:]+pi[:i]
            if gh==s1:
                flag=1
                break
        if flag==1:
            break
    if flag==1:
        print("true")
    else:
        print("false")
