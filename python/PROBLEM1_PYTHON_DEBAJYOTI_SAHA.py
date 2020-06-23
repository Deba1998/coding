arr=input()
arr=arr[1:-1]
arr=list(arr.split(","))
for i in range(len(arr)):
    arr[i]=int(arr[i])
if len(arr)<=2:
    print("Wrong Input")
else:
    count=0
    for i in range(1,len(arr)-1):
        if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
            count+=1
    print(count)