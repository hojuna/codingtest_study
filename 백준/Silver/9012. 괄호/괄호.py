import sys
def sol():

    n=int(sys.stdin.readline())

    for _ in range(n):
        temp=sys.stdin.readline()
        aa=[]
        bl=True
        for i in temp:
            if i=="(":
                aa.append(i)

            elif i==")" :
                if aa==[]:
                    bl=False
                    break
                else:
                    aa.pop()
        if aa==[] and bl:
            print("YES")
        else:
            print("NO")

sol()



