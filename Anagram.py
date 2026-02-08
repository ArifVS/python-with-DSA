s1 = 'listen'
s2 = 'silent'
s1 = list(s1)
s2 = list(s2)
s1.sort()
s2.sort()
if(s1==s2):
    print('Anagram')
else:
    print("Not Anagram")
