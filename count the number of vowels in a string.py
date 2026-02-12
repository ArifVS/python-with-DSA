n = "Arif"
count = 0
for i in range(len(n)):
    if n[i] in 'aeiouAEIOU':
        count+=1
print(count)
