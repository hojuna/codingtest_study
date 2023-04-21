import sys

def sol():
    n,m,b=map(int,sys.stdin.readline().split(" "))
    lista=[]

    for i in range(n):
        lista.append(list(map(int,sys.stdin.readline().split(" "))))

    result_g=sys.maxsize
    index=0
    for g in range(257):
        min_,max_=0,0
        for i in range(n):
            for j in range(m):
                if lista[i][j]>g :
                    max_+=lista[i][j]-g
                else:
                    min_+=g-lista[i][j]

        if max_+b < min_:
            continue
        
        k=min_+(max_*2)
        if k <= result_g:
            result_g= k
            index= g

            
    print(result_g,index)
  

sol()