temp=input()

for i in range(ord('a'),ord('z')+1):
    cnt=temp.count(chr(i))
    if cnt == 0 :
        print(-1, end=" ")
    else:
        print(temp.index(chr(i)), end =" ")