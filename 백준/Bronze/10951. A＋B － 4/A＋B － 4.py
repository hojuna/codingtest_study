while True:
    try:
        temp=tuple(map(int,input().split()))
    except:
        break
    print(temp[0]+temp[1])