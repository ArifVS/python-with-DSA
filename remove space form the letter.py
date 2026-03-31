# remove space form the letter
s = "Velloresyed Arifulla"
for i in range(len(s)):
    if(s[i]==" "):
        continue
    print(s[i],end="")
