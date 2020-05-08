def solve(s,i,j,ind):
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
        LT = solve(s, i, k-1, True)
        LF = solve(s, i, k-1, False)
        RT = solve(s, k+1, j, True)
        RF = solve(s, k+1, j, False)
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
s = "F&F&T^T"
n=len(s)
x=dict()
print(solve(s,0,n-1,True))
print(x)

