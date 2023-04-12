num=int(input())
a = list(map(int, input().split()))
max_num=max(a)
sum_num=0
for i in a:
    sum_num+=i/max_num*100
    
print(sum_num/num)