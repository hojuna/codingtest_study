from collections import deque



dq= deque([])

n,m= map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
result=[[0]*m for _ in range(n)]

def range_out(x,y):
    if x<0 or x>=n or y<0 or y>=m or arr[x][y]==0 or visit[x][y]==1:
        return False
    return True

xs=[1,-1,0,0]
ys=[0,0,1,-1]
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            dq.append([i,j])
            visit[i][j]=1
            result[i][j]=0

while dq:
    x,y=dq.popleft()
    for dx,dy in zip(xs,ys):
        r,c=x+dx,y+dy
        if range_out(r,c):
            result[r][c]=result[x][y]+1
            dq.append([r,c])
            visit[r][c]=1

for i in range(n):
    for j in range(m):
        if visit[i][j]==0 and arr[i][j] ==1:
            result[i][j]=-1


for i in range(n):
    print(*result[i])





