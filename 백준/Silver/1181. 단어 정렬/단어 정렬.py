n=int(input())

aa=[]
for _ in range(n):
    aa.append(input())

aa=list(set(aa))
aa=sorted(sorted(aa),key=len)

for i in aa:
    print(i)