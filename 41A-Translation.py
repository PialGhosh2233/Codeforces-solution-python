s=input()
t = input()
def translate(str):  
    str1 = ""   
    for i in str:  
        str1 = i + str1  
    return str1
a=translate(t)    
if s==a:
    print("YES")
else:
    print("NO")