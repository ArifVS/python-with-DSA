# Move Negative elements to one side of the array
arr = [2,-3,4,5,6,-7,8,9]
j = len(arr)-1
for i in range(len(arr)-1,-1,-1):
    if(arr[i]<0):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j = j-1
print(arr)
