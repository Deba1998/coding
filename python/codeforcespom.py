for i in range(int(input())):
    d,a,m,b,x=map(int,input().split())
    if x<=d:
        print(0)
    elif x<=(d+a):
        print(1)
    else:
        low=1
        high=((x-d)//b)+1
        res=high
        while low<=high:
            mid=low+(high-low)//2
            gf=mid//(m+1)
            sumi=((gf*b)+(mid-gf)*a)
            if sumi>=(x-d):
                if mid<res:
                    res=mid
                high=mid-1
            else:
                low=mid+1
        print(res)