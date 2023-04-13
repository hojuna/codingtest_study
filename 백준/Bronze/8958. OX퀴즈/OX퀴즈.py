n=int(input())
for i in range(n):
    temp=input()
    index=0
    sum_num=0
    for i in temp:
        if i=="O":
            index+=1
        elif i=="X":
            index=0
        sum_num+=index
    print(sum_num)
        