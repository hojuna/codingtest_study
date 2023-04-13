temp=[]
for i in range(42):
    temp.append(0)

for i in range(10):
    temp[int(input())%42]+=1

cnt=0
for i in temp:
    if i != 0:
        cnt+=1
print(cnt)
