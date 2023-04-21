import sys

def sol():
    n=int(sys.stdin.readline().rstrip())

    lista=[]
    for i in range(n):
        k,p=map(int,sys.stdin.readline().split(" "))
        lista.append((k,p))

    lista.sort(key=lambda x : (x[1],x[0]))


    for i in lista:
        print(i[0],i[1])
    
sol()