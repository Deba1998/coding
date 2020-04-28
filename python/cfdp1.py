for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=1
    sum=0
    for i in range(n):
        sum+=l[i]
        if sum<=0:
            flag=0
            break
    sumi=0
    for j in range(n-1,-1,-1):
        sumi+=l[j]
        if sumi<=0:
            flag=0
            break
    if flag==0:
        print("NO")
    else:
        print("YES") 



    