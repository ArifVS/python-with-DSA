# First non repeating character index
str = "mam"
for i in range(len(str)):
    c = 0
    for j in range(len(str)):
        if(str[i]==str[j]):
            c+=1
    if c==1:
        print(i)
        break
