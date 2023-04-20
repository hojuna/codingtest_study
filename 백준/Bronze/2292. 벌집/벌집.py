import sys



def sol():
    n=int(sys.stdin.readline())
    
    
    k=6
    temp=1
    while temp<n:
       temp+=k
       k+=6
    print(k//6) 

sol()
