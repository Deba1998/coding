t=int(input())
for z in range(1,t+1):
    d=input()
    s="("*int(d[0])
    s+=d[0]
    if len(d)==1:
        s+=")"*int(d[0])
        print(s)
    else: 
        for i in range(1,len(d)):
           if int(d[i])==int(d[i-1]):
              s+=d[i]
           elif int(d[i])<int(d[i-1]):
              s+=")"*(int(d[i-1])-int(d[i]))
              s+=d[i]
           else:
              s+="("*(int(d[i])-int(d[i-1]))
              s+=d[i]
        s+=")"*int(d[-1])
        print(s)




    

        

