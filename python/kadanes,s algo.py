def maxSubarraySum(arr):
    c = 0
    m = 0
    for i in arr:
        c = max(i,c+i)
        m = max(m,c)
    return m

arr = [-2,-3,4,-1,-2,1,5,-3]
print(maxSubarraySum(arr))