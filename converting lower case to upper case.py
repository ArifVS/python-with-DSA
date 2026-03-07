# converting lower case to upper case
text = "Arif"
res = ""
for ch in text:
    if 'a'<=ch<='z':
        res = res+chr(ord(ch)-32)
    else:
        res = res + ch
print(res)
        
