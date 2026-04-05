s = "abcd"
res = ""
for i in range(len(s)):
    mr = chr(ord('a')+ord('z')-ord(s[i]))
    res = res+mr
print(res)
