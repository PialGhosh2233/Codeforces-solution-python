while True:
    n=int(input())
    s=input().upper()
    if len(s)==n:
        break
a=0
d=0
for i in s:
    if i=="A":
        a=a+1
    elif i=="D":
        d=d+1
if a>d:
    print("Anton")
elif d>a:
    print("Danik")
else:
    print("Friendship")