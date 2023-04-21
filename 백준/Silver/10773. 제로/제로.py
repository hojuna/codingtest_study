import sys

def sol():
    n=int(sys.stdin.readline().rstrip())
    stack=[]
    for i in range(n):
        k=int(sys.stdin.readline().rstrip())

        if k!=0:
            stack.append(k)
        else:
            stack.pop()
    
    print(sum(stack))

    
    
sol()