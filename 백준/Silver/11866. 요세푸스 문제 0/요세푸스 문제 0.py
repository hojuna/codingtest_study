import sys
from collections import deque


def sol():

    n,m=map(int,sys.stdin.readline().split(" "))

    que=deque(i for i in range(1,n+1))
    result=[]
    cnt=1
    while que:
        if cnt==m:
            result.append(que.popleft())
            cnt=1
        else:
            que.append(que.popleft())
            cnt+=1
    
    print("<",end="")
    for i in range(n-1):
        print(result[i],end=", ")
    print(str(result[n-1])+">")

sol()