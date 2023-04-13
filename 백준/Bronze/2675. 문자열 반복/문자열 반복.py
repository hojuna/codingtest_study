n=int(input())

for i in range(n):
    temp=list(input().split(" "))
    for k in temp[1]:
        for j in range(int(temp[0])):
            print(k,end="")
    print()
        