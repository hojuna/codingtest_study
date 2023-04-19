import sys

def sol():
    
    maxM=1
    minM=0
    n,m=map(int,sys.stdin.readline().split(" "))
    maxN=max(n,m)

    a=0
    for i in range(1,maxN+1):
        if n%i==0  and m%i==0:
            maxM=i

    k=maxN
    while True:
        if k%n==0  and k%m==0:
            minM=k
            break
        k+=1
    print(maxM)
    print(minM)

sol()