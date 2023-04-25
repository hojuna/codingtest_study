import sys


def sol():

    n= int(sys.stdin.readline().strip())

    
    k=1
    if n>=1:
        for i in range(1,n+1):
            k*=i

    cnt=0

    aa=list(str(k))
    for i in aa[::-1]:
        if '0' ==  i:
            cnt+=1
        else:
            break


    return(cnt)

print(sol())