import sys
def sol():

    t=int(sys.stdin.readline())

    for _ in range(t):
        h,w,n=map(int, sys.stdin.readline().split(" "))
        cnt=1

        while n>h:
            n-=h
            cnt+=1
        print(str(n*100+cnt))
sol()



