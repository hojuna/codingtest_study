from collections import deque
import sys


t = int(input())

def sol():
    for _ in range(t):
        n, m = map(int, input().split())
        queue = deque(list(map(int, sys.stdin.readline().split())))
        cnt=0
        while queue:

            if max(queue)==queue[0]:
                queue.popleft()
                cnt+=1
                if m==0:
                    print(cnt)
                    break
                else:
                    m-=1
            else:
                queue.append(queue.popleft())
                if m==0:
                    m=len(queue)-1
                else:
                    m-=1
sol()