data= input().split(" ")
dd="----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.".split(" ")
ans=""
for i in data:
    pt = dd.index(i)
    ans +=  str(pt)
print(ans)


