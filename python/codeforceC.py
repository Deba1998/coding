t=int(input())
for i in range(t):
    h,c,t=map(int,input().split())
    if h<=t and c<=t:
        print(1)
    else:
        avg=(h+c)/2
        diff=abs(t-(t+avg)/2)
        res=2
        low=1
        high=15
        while low<=high:
            mid=(low+high)//2
            print(mid)
            if mid%2==0:
                sumi=(avg*(mid))
            else:
                sumi=h+(avg*(mid))
            if ((sumi+t)/mid+1)<=t:
                low=mid+1
                if abs(t-(sumi+t)/mid+1)<diff:
                    diff=abs(t-(sumi+t)/mid+1)
                    res=mid
            else:
                high=mid-1
                if abs(t-(sumi+t)/mid+1)<diff:
                    diff=abs(t-(sumi+t)/mid+1)
                    res=mid             
        print(res)
     