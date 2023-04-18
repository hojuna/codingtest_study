import sys

def sol():
    n, *target = map(int, sys.stdin.buffer.read().splitlines())
    stack=[]
    print_list=[]


    temp=0
    for i in range(1,n+1):
        stack.append(i)
        print_list.append("+")
        while True:
            if stack != [ ] and stack[-1]==target[temp] and temp<n:
                stack.pop()
                print_list.append("-")
                temp+=1
            else:
                break

    for i in range(n-temp):
        if stack[-1]==target[temp]:
            stack.pop()
            print_list.append("-")
            temp+=1

    if temp==n:
        for i in print_list:
            print(i)
    else:
        print('NO')

sol()