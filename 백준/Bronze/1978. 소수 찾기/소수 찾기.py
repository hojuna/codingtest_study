n=int(input())
a=list(map(int,input().split(" ")))
cnt=0
for i in a:
    bl=True
    if i==1:
        bl=False

    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            bl=False
    if bl:
        cnt+=1
print(cnt)