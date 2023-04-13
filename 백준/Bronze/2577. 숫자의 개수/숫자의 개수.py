num=1
for i in range(3):
    num*=int(input())
    
result=[0,0,0,0,0,0,0,0,0,0]

for i in str(num):
    result[int(i)]+=1

for i in result:
    print(i)