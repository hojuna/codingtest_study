import sys


def sol():
    global n,lista
    n=int(sys.stdin.readline())
    lista=list(map(int,sys.stdin.readline().split(" ")))

    m=int(sys.stdin.readline())
    listb=list(map(int,sys.stdin.readline().split(" ")))

    dic={}
    for i in list(set(lista)):
        dic[i]=0
    
    for i in lista:
        dic[i]+=1
    
    for i in listb:
        if i in dic:
            print(dic.get(i),end=" ")
        else:
            print(0,end=" ")
    
sol()