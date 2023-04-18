
import sys

def find_num(nums,num):
    start=0
    end=len(nums)-1

    while start<=end:
        mid=(start+end)//2
        if num > nums[mid]:
            start=mid+1
        elif num==nums[mid]:
            return True
        else:
            end=mid-1


    return False
            

def sol():
    
    n=int(sys.stdin.readline())
    nums = sorted(list(map(int,sys.stdin.readline().split())))
    m=int(sys.stdin.readline())
    mums = list(map(int,sys.stdin.readline().split()))

    for i in mums:
        if find_num(nums,i):
            print(1)
        else:
            print(0)

sol()