import sys
def sol():
    n,m=map(int,sys.stdin.readline().split(" "))
    lista=sorted(list(map(int,sys.stdin.readline().split(" "))))
    result=0
    for i in lista:
        for j in lista:
            if i==j:
                continue
            for k in lista:
                if j==k or i==k:
                    continue
                temp=i+j+k
                if temp<=m and result<temp:
                    result=temp
    print(result)
sol()



