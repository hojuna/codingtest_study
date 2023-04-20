import sys
from collections import deque

def push(num):
    k.append(num)

def pop():
    if not k:
        return -1 
    return k.popleft()

def size():
    return len(k)

def empty():
    if not k :
        return 1
    
    return 0

def front():
    if not k :
        return -1
    return k[0]

def back():
    if not k :
        return -1
    return k[-1]


def sol():

    n=int(sys.stdin.readline())
    
    global k
    k=deque()
    result=[]
    for _ in range(n):
        temp=sys.stdin.readline()
        if " " in temp:
            commnd, num=temp.split(" ")
            num=num.rstrip()
            push(num.rstrip())
        else:
            commnd= temp.rstrip()
            print(eval(commnd+"()"))




sol()