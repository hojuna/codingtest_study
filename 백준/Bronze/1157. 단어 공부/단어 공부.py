temp=input().lower()
aa=[]
set_temp=set(temp)
for i in set_temp:
    aa.append(temp.count(i))

if aa.count(max(aa))!=1:
    print("?")
else :
    set_temp=list(set_temp)
    print(set_temp[aa.index(max(aa))].upper())
