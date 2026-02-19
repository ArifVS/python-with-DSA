arr = [1, 0, 3, 0, 5, 0, 7, 9]
z = []
nz = []
for i in range(len(arr)):
    if(arr[i]==0):
        z.append(arr[i])
    else:
        nz.append(arr[i])
print(nz+z)
        
        
