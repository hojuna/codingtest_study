from collections import deque
def sol():
    que=deque()
    n=int(input())

    for i in range(n,0,-1):
        que.append(i)
    

    bl=True
    while len(que)>1:
        if bl:
            que.pop()
            bl= not bl
        else:
            que.appendleft(que.pop())
            bl= not bl
    
    print(que.pop())
sol()