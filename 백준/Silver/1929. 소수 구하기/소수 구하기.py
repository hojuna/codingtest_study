import math,sys

def sol():
    a,b=map(int,sys.stdin.readline().split(" "))
    
    for i in range(a,b+1):
        if i!=1:
            bl=True
        else:
            bl=False
        for j in range(2,int(math.sqrt(i)) + 1):
            # print(i,j)
            if i%j==0:
               bl=False
               break
        if bl:
            print(i) 
sol()