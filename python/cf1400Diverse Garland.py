n=int(input())
s=input()
if n==1:
    print("0")
    print(s)
else: 
    count=0
    l=[]
    indexl=[]
    dis=list(s)
    for i in range(1,n-1):
        if dis[i]==dis[i-1]:
            count+=1
            if s[i]=="R":
                if s[i+1]=="R":
                    dis[i]="G"
                if s[i+1]=="G":
                    dis[i]="B"
                if s[i+1]=="B":
                    dis[i]="G"
            if s[i]=="B":
                if s[i+1]=="R":
                    dis[i]="G"
                if s[i+1]=="G":
                    dis[i]="R"
                if s[i+1]=="B":
                    dis[i]="G"
            if s[i]=="G":
                if s[i+1]=="R":
                    dis[i]="B"
                if s[i+1]=="G":
                    dis[i]="B"
                if s[i+1]=="B":
                    dis[i]="R"
    if dis[n-1]==dis[n-2]:
        count+=1
        if s[n-1]=="R":
            dis[n-1]="B"
        if s[n-1]=="G":
            dis[n-1]="B"
        if s[n-1]=="B":
            dis[n-1]="R"
    if count==0:
        print("0")
        print(s)
    else:
        print(count)
        print("".join(dis))
