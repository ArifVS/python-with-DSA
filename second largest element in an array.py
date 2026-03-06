# second largest element in an array
arr = [1,10,2,54,29,3,2,85]
fl = arr[0]
sl = -99999
for i in range(len(arr)):
    if arr[i]>fl:
        sl = fl
        fl = arr[i]
    elif arr[i]>sl and arr[i]!=fl:
        sl = arr[i]
print("Second largest:",sl)
