org = int(input("請輸入十進位的正整數："))
num=org
ans=""
while num//3 != 0:
    ans=str(num%3)+ans
    num=num//3
ans = int(str(num)+ans)
print("%d的三進位為%d" %(org,ans))

