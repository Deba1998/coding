for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=dict()
    for i in range(n):
        if l[i] not in x:
            x[l[i]]=1
        else:
            x[l[i]]+=1
    l=[]
    for c in x:
        l.append([x[c],c])
    l.sort(reverse=True)
    if len(l)==1:
        print(l[0][1])
    else:
        if l[0][0]>=(2*l[1][0]):
            print(l[0][1])
            