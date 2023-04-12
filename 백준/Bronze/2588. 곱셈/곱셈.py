n= int(input())
m= int(input())
k=m
for i in range(3):
    temp=m%10
    print(n*(temp))
    m=int(m/10)
print(n*k)