import sys
 
def sol():

    lista=[(0,0) for _ in range(41)]
    lista[0]=(1,0)
    lista[1]=(0,1)
    lista[2]=(1,1)
    t = int( sys.stdin.readline().rstrip())
    
    for i in range(2,41):
        if lista[i]==(0,0):
             lista[i]=( 
                lista[i-1][0]+lista[i-2][0],
                lista[i-1][1]+lista[i-2][1]
                       )
             
    for _ in range(t):

        
        temp=lista[int(sys.stdin.readline().rstrip())]
        print(temp[0],temp[1])



sol()