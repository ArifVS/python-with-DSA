# Counting number of vowels and consonets
s = 'hello'
vowel = 0
cons = 0 
for i in range(len(s)):
    if(s[i]!=''):
        if(s[i]=='a'or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
            vowel+=1
        else:
            cons+=1
print("vowels:",vowel)
print("consonents:",cons)
        
