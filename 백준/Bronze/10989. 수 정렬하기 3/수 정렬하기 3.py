import sys

def sol():
    n=int(sys.stdin.readline().rstrip())
    lista=[0]*10001

    for i in range(n):
        lista[int(sys.stdin.readline().rstrip())]+=1
    
    for i in range(1,10001):
        if lista[i]!=0:
            for j in range(lista[i]):
                print(i)
    
    
    
sol()