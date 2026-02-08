# Palindrome
s = 'frrf'
res = ''

for i in range(len(s)-1,-1,-1):
    res = res+s[i]
print(res)

if (res==s):
    print("Palindrom")
else:
    print("Not a palindrom")
    
    
