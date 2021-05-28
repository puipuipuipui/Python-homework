n=int(input("請輸入正整數n："))
ans=1
i=2
while i**2 <=n:
    if n%i==0:
        ans+=i+n/i
    i+=1
if  ans == n:
    print("perfect")
elif ans > n:
    print("abundant")
else:
    print("deficient")
