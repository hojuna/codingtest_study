check=True

aa=list(map(int,input().split(" ")))

if aa==sorted(aa):
    print("ascending")
elif aa==sorted(aa,reverse=True):
    print("descending")
else:
    print("mixed")