k,n,w=map(int,input().split(" "))
price=0
for i in range(1,w+1):
     price=price+(k*i)
if price>n:
    j=price-n
    print(j)
else:
    print(0)