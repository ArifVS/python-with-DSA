s = input("Enter a string")
freq = {}
for ch in range(len(s)):
    if s[ch] in freq:
        freq[s[ch]]+=1
    else:
        freq[s[ch]] = 1
for key,val in freq.items():
    print(key,val)
