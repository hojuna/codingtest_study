import sys



def sol():
    t=int(sys.stdin.readline())
    lista=[]
    for _ in range(t):
        n,m=map(int,sys.stdin.readline().split(" "))
        lista.append((n,m))
    
    lista.sort(key=lambda x: (x[0],x[1]) )

    for x,y in lista:
        print(x,y)

sol()