import sys
def sol():
    n=int(sys.stdin.readline())
    lista=[]

    #평균, 중앙값, 최빈값, 범위
    for _ in range(n):
        lista.append(int(sys.stdin.readline()))
    lista=sorted(lista)
    print(round(sum(lista)/n))
    print(lista[len(lista)//2])
    cntN={}
    cnt=0
    
    for i in range(0,len(lista)):
        if i==len(lista)-1:
            cntN[lista[i]]=cnt
            cnt=0
        else:
            if lista[i]==lista[i+1]:
                cnt+=1
            else:
                cntN[lista[i]]=cnt
                cnt=0
        
    #이게 뭐징
    if len(lista)==1:
        cntList=lista
    else:
        cntList=[k for k,v in cntN.items() if max(cntN.values())==v]
    print(cntList[0] if len(cntList)==1 else cntList[1] )
    print(lista[-1]-lista[0])

sol()
