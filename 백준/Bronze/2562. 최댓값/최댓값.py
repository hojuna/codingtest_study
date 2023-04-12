
a={}
max_num=0
for i in range(9):
    temp=int(input())
    a[temp]=i+1
    if max_num<temp:
        max_num=temp

print(max_num)
print(a[max_num])