from collections import deque
import sys

def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node+1,end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)





def dfs(node):
    if node not in visited:
        visited.add(node)
        print(node+1,end=" ")
        for neighbor in graph[node]:
            dfs(neighbor)

def sol():
    global graph,visited

    N,M,startN= map(int,sys.stdin.readline().split(" "))
    graph=[[] for i in range(N)]

    for i in range(M):
        k,p=map(int,sys.stdin.readline().split(" "))
        graph[k-1].append(p-1)
        graph[p-1].append(k-1)
        graph[k-1].sort()
        graph[p-1].sort()



    visited = set()
    dfs(startN-1)
    print()
    
    visited = set()
    bfs(startN-1)
sol()


