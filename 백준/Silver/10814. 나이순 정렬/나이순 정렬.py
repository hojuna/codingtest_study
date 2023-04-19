import sys,operator  
def sol():

    t=int(sys.stdin.readline())
    dict={}
    tup=[]
    for _ in range(t):
        age,name=sys.stdin.readline().split(" ")
        name=name.rstrip()
        tup.append((int(age),name))

    # dict=sorted(dict.items(), key=lambda x: x[1])
    # dict=sorted(dict.items(), key=operator.itemgetter(1))
    
    tup.sort(key=lambda tup: tup[0])
    for k,v in tup :
        print(k,v)    
        
sol()



