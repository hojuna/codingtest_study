import sys

def sol2():

    n,m=map(int,sys.stdin.readline().split(" "))
    lista=list(map(int,sys.stdin.readline().split(" ")))


    start=0
    res=0
    end=max(lista)
    while start<=end:

        mid=(start+end)//2
        total=0

        for i in lista:
            if i > mid:
                total+=i-mid
        
        if total<m:
            end= mid-1
        else:
            res= mid
            start=mid+1
    print(res)


sol2()
