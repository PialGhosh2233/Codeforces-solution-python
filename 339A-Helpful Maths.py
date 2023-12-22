s=input().split("+")
s.sort()
str=""
for i in range(0,len(s)):
    if i!=len(s)-1: 
     str+=s[i]+"+"
    else:
        str+=s[len(s)-1]
print(str)  