import sys



def sol():
    n,m=map(int,sys.stdin.readline().split(" "))
    result=1
    for i in range(n,n-m,-1):
        result*=i
    
    temp=1
    for i in range(1,m+1):
        temp*=i

    print(result//temp)

sol()