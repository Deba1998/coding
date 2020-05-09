def solve(s,i,j,ind,x):
    if i>j:
        return(False)
    if i==j:
        if ind==True:
            return s[i] == 'T'
        else:
            return s[i] == 'F'
    keyi=str(i)+" "+str(j)+" "+str(ind)
    if keyi in x:
        return(x[keyi])
    count = 0
    for k in range(i+1, j, 2):
        LT = solve(s, i, k-1, True,x)
        LF = solve(s, i, k-1, False,x)
        RT = solve(s, k+1, j, True,x)
        RF = solve(s, k+1, j, False,x)
        if s[k] == '&':
            if ind==True:
                count = count + LT * RT
            else:
                count = count + LT * RF + LF * RT + LF * RF
        elif s[k] == '|':
            if ind==True:
                count = count + LT * RF + LF * RT + LT * RT
            else:
                count = count + LF * RF
        elif s[k] == '^':
            if ind==True:
                count = count + LT * RF + LF * RT
            else:
                count = count + LT * RT + LF * RF
        
    x[keyi] = count
    return count
s = "T^T^T^F|F&F^F|T^F^T"
n=len(s)
x=dict()
print(solve(s,0,n-1,True,x))


