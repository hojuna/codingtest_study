temp=list(map(int,input().split()))

sumN=0

for i in temp:
    sumN+=i*i

print(sumN%10)
