r=0
for i in range(int(input())):
    p,q=map(int,input().split(" "))
    t=q-p
    if t>=2:
        r+=1
print(r)  