def main():
    n,k=map(int,input().split(" "))

    alist=[]
    for _ in range(n):
        alist.append(int(input()))

    maxNum=max(alist)
    minNum=0

    while minNum <= maxNum:
        cnt=0
        num=(minNum+maxNum)//2
        
        if num==0:
            break
        for i in range(n):
            cnt+=alist[i]//num

        
        if cnt>=k:
            minNum=num+1
        elif cnt<k:
            maxNum=num-1
        
    print(maxNum)


main()
