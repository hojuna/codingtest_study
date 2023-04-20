import sys

def push(num):
    k.append(num)

def pop():
    if not k:
        return -1
    return k.pop()

def size():
    return len(k)

def empty():
    if k:
        return 0
    else:
        return 1

def top():
    if not k :
        return -1
    return k[-1]

def sol():

    n=int(sys.stdin.readline())
    
    global k
    k=[]
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