import sys
# 그리드 알고리즘



def sol():
    n=int(sys.stdin.readline())
    
    cnt_5=[x for x in range(0,n//5+1)]
    cnt_5.reverse()
    cnt_3=[x for x in range(0,n//3+1)]

    cnt=n

    for i in cnt_5:
        for j in cnt_3:
            if n==i*5+j*3:
                if cnt>i+j:
                    cnt=i+j
    for i in cnt_3:
        for j in cnt_5:
            if n==i*3+j*5:
                if cnt>i+j:
                    cnt=i+j 

    if cnt==n:
        print(-1)
    else:       
        print(cnt)            




sol()

