for i in range(int(input())):
    x, y=map(int,input().split())
    n=0
    k=1
    while(n+k<y):
        n=n+k
        k+=1
    z=y-n-1
    k=x-1-k
    z=x-1-z
    for i in range(x):
        if i==k or i==z:
            print("b",end="")
        else:
            print("a",end="")
    print("")

