n,x=map(int,input().split(" "))
temp=list(map(int,input().split(" ")))

for i in temp:
    if i < x:
        print(i,end=" ")