def lcs(i, j, count) :  
      
    if (i == 0 or j == 0) :  
        return count  
          
    if (X[i - 1] == Y[j - 1]) : 
        count = lcs(i - 1, j - 1, count + 1)  
      
    count = max(count, max(lcs( i, j - 1, 0),  
                           lcs( i - 1, j, 0)))  
  
    return count 
  
# Driver code  
if __name__ == "__main__" : 
  
    X = "abracadabra"
    Y = "avadakedavra"
  
    n = len(X) 
    m = len(Y) 
  
    print(lcs(n, m, 0))  