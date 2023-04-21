import sys
sys.setrecursionlimit(10**6)

def index_check(i,j):
    return 0<=i and i <x and 0<=j and j <y



def find_k(x,y):
    global check
    num_x=[0,0,1,-1]
    num_y=[1,-1,0,0]

    if check[x][y]==0:
        check[x][y]=1

    for i,j in zip(num_x,num_y):
        if index_check(x+i,y+j) and check[x+i][j+y]==0:
            find_k(x+i,y+j)
            



t=int(sys.stdin.readline().strip())
k,p=0,0

for _ in range(t):

    x,y,n=map(int,sys.stdin.readline().strip().split(" "))

    lista=[[[0] for i in range(y+1)] for i in range(x+1)]
    check=[[[1] for i in range(y+1)] for i in range(x+1)]
    for _ in range(n):
        k,p=map(int,sys.stdin.readline().strip().split(" "))
        lista[k][p]=1
        check[k][p]=0

    cnt=0
    for i in range(x):
        for j in range(y):
            if lista[i][j]==1 and check[i][j]==0:
                cnt+=1
                find_k(i,j)

    # for i in lista:
    #     print(i)
    print(cnt)

    # print(index_check(1,1))
    # print(index_check(11,11))
    # print(aa())