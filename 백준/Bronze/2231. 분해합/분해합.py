import sys

def sum_Num(num):
    sumN=0
    temp=num
    while True:
        if temp<10:
            break
        sumN+=temp%10
        temp=temp//10
    return sumN+temp

def sol():
    n=int(sys.stdin.readline())

    cnt=0
    temp=(n-(len(str(n))*9))
    while temp+sum_Num(temp)!=n and temp<n :
        temp+=1

    if temp+sum_Num(temp)!=n :
        print(0)
    else:
        print(temp)


sol()
