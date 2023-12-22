c=int(input())
for i in range(0,c):
    n=input().split(" ")
    a=int(n[0])
    b=int(n[1])
    v=a/b
    if v-int(v)==0:
       print(0)
    else:
        n=b*(int(v)+1)
        ans=n-a
        print(ans)