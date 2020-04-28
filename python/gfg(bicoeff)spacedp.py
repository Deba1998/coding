#space optimized
def  bicoeff(n,k):
    c=[0]*(k+1)
    c[0]=1
    for i in range(1,n+1):
        for j in range(k,0,-1):
            c[j]=c[j]+c[j-1]
    return(c[k])
print(bicoeff(4,2))