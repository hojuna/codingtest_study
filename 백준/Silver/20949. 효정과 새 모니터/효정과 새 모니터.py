import math

n= int(input())
arr=[]
for i in range(n):
    w,h=map(int,input().split())
    arr.append((math.sqrt(w**2+h**2)/77,i+1))
arr.sort(key=lambda x:(-x[0],x[1]))


for i in range(n):
    print(arr[i][1])