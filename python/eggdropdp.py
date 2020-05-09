'''#top down
def Solve(eggs, floors):
  if floors == 0 or floors == 1:
    return floors
  if eggs == 1:
    return floors
  if dp[eggs][floors] != -1:
    return dp[eggs][floors]
  count = float('inf')
  for i in range(1, floors+1):
      if dp[eggs][floors-i]!=-1:
          high=dp[eggs][floors-i]
      else:
          high=Solve(eggs,floors-i)
      if dp[eggs-1][i-1]!=-1:
          low=dp[eggs-1][i-1]
      else:
          low=Solve(eggs-1,i-1)
      temp = 1 + max(high,low)
      count = min(count, temp)
  dp[eggs][floors] = count
  return count
eggs=5
floor=5
dp=[[-1 for i in range(floor+1)]for i in range(eggs+1)]
print(Solve(eggs,floor))'''
#bottom up
def Solve(eggs, floors):
    T=[[0 for _ in range(floors+1)] for _ in range(eggs+1)]
    for j in range(floors+1):
        T[1][j] = j
    for i in range(1,eggs+1):
        T[i][1]=1
    for i in range(2, eggs+1):
        for j in range(2, floors+1):
            T[i][j] = float('inf')
            for k in range(1, j+1):
                count = 1 + max(T[i-1][k-1], T[i][j-k])
                T[i][j] = min(T[i][j], count)
    return T[i][j]
eggs=5
floor=5
print(Solve(eggs,floor))