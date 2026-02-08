# Palindrom String
s = "madam"
i = 0 
j = len(s)-1
pal = True
while i<j:
    if (s[i] != s[j]):
          pal = False
          break
    i+=1
    j-=1
if pal==True:
  print("Palindrom")
else:
  print("Not palindrom")
