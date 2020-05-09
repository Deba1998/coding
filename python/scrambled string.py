def Solve(X, Y):
  if len(X) != len(Y):
    return False
  if len(X) == 0 and len(Y) == 0:
    return True
  if X == Y:
    return True
  if len(X)<=1:
    return False
  keyi=X+" "+Y
  if keyi in p:
    return(p[keyi])
  n = len(X)
  flag = False
  for i in range(1, n):
    caseSwap = (Solve(X[:i], Y[n-i:]) == True) and (Solve(X[i:], Y[:n-i]) == True)
    caseNoSwap = (Solve(X[:i], Y[:i]) == True) and (Solve(X[i:], Y[i:]) == True)
    if caseSwap or caseNoSwap:
      flag = True
      break
  p[keyi]=flag
  return flag
X = "great"
Y = "rgate"
p=dict()
print(Solve(X,Y))
print(p)
