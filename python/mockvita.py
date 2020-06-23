import math
result=""
t=int(input())
for i in range(t):
    n=int(input())
    ans=math.floor(math.log(n,2))
    print((ans+1))