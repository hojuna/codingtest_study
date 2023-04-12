t=int(input())

for _ in range(t):
    k=int(input())
    n=int(input())
    arr=[[0]*14 for _ in range(k+1)]
    for i in range(k+1):
        for j in range(14):
            if i==0:
                arr[0][j]=j+1
            elif j==0:
                arr[i][j]=1
            else:
                arr[i][j]=arr[i-1][j]+arr[i][j-1]
    print(arr[k][n-1])

