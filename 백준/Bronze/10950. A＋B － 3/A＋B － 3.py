n=int(input())

for i in range(n):
    temp=tuple(map(int,input().split()))
    print(temp[0]+temp[1])