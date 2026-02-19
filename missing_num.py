arr = [1,2,4,5,6]
n = len(arr)+1
expected_sum = n*(n+1)//2
print(expected_sum)
actual_sum = 0
for i in range(len(arr)):
    actual_sum = actual_sum+arr[i]
print(actual_sum)
missing_num = expected_sum-actual_sum
print(missing_num)
