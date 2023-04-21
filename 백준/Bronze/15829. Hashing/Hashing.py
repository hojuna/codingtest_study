import sys

def sol():
    n=int(sys.stdin.readline().rstrip())

    sumN=0
    str_=sys.stdin.readline().rstrip()
    for i in range(n):
        k=(ord(str_[i])-96)*(31**i)
        sumN+=k

    print(sumN%1234567891)
sol()