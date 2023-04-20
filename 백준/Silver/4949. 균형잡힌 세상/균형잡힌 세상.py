import sys

def check_str(str_):

    k=[]

    for i in str_:
        if "("==i:
            k.append("(")

        elif ")"==i:
            if not k:
                return False
            elif k[-1]!="(":
                return False
            k.pop()

        elif "["==i:
            k.append("[")


        elif "]"==i:
            if not k:
                return False
            elif k[-1]!="[":
                return False
            k.pop()

    if not k :
        return True
    else:
        False

def sol():
    aa=[]
    while True:
        v=sys.stdin.readline().rstrip()
        if v==".":
            break
        if check_str(v):
            print('yes')
        else:
            print("no")
    
sol()

