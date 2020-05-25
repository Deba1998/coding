def SubArraySum(arr, n ): 
    result = 0
  
    # computing sum of subarray  
    # using formula 
    for i in range(0, n): 
        result += (arr[i] * (i+1) * (n-i)) 
        print(result)
    # return all subarray sum 
    return result 
l=[1,2,3]
SubArraySum(l,len(l))