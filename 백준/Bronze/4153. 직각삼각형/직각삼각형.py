import sys
def sol():
    while True:
        lista=sorted(list(map(int,sys.stdin.readline().split(" "))))
        if sum(lista)==0:
            break
        if lista[0]**2+lista[1]**2==lista[2]**2:
            print("right")
        else:
            print("wrong")

sol()



