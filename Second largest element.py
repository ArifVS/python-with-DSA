# Second largest 
arr = [1,5,20,8]
l = float('-inf')
s = float('-inf')
for i in range(len(arr)):
    l = max(l,arr[i])
for i in range(len(arr)):
    if arr[i]>s and l!=arr[i]:
        s = arr[i]
print(s)
