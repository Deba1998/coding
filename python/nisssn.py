for i in range(int(input())):
    n, k, p=map(int,input().split())
    kl=list(map(int,input().split()))
    y=dict()
    for i in kl:
        y[i]=1
    low=1
    high=n
    res="abc"
    while low<=high:
        mid=low+(high-low)//2
        count=0
        for i in y:
            if i<=mid:
                count+=1
        if (mid-count)==p and mid not in y:
            res=mid
            break
        elif (mid-count)==p and mid in y:
            high=mid-1
        elif(mid-count)<p:
            low=mid+1
        else:
            high=mid-1
    if res!="abc":
        print(res)
    else:
        print(-1)