arr = [10,7,1,2,5,2,7,9,10,32]

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
print(arr)
