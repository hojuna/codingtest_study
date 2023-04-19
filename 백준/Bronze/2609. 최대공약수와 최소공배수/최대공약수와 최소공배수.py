import sys,math

def sol():
    
    maxM=0
    minM=0
    n,m=map(int,sys.stdin.readline().split(" "))
    print(math.gcd(n,m))
    print(math.lcm(n,m))

sol()