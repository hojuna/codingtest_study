import sys

def sol():
    t = int(sys.stdin.readline().rstrip())

    lista=[]
    for _ in range(t):
        kg,tall=map(int,sys.stdin.readline().split(" "))
        lista.append((kg,tall))
    

    result=[]
    for i in range(0,t):
        cnt=1
        for j in range(0,t):
            if i==j:
                continue
            if lista[i][0] < lista[j][0] and lista[i][1] < lista[j][1]:
                cnt+=1

        result.append(cnt)
    
    for i in result:
        print(i,end=" ")

sol()