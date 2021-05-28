def gcd(a,b):
    if b==0:
        return a
    else:   
        c=a%b
        return gcd(b,c)

data=input().split(",")
ans=[]
for i in range(0,len(data)-1):
    for j in range(i+1,len(data)):
        ans.append(gcd(int(data[i]),int(data[j])))
print(max(ans))
