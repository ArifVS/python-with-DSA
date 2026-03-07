#most frequently repearing character
s = "hello"
dic= {}
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = 1
    else:
        dic[s[i]]+=1
print(dic)
print(dic.keys())

max_count = 0
max_key = ""

key = list(dic.keys())
for i in range(len(key)):
    if dic[key[i]] > max_count:
        max_count = dic[key[i]]
        max_key = key[i]
        
print(max_count,max_key)
