n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(1)
else:    
    c=1
    maxi=1
    for i in range(1,n):
        if l[i]<=(2*l[i-1]):
            c+=1
        else:
            c=1
        maxi=max(maxi,c)
    print(maxi)
