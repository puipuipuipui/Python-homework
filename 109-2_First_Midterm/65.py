a=input("請輸入A的好友:").split(" ")
b=input("請輸入B的好友:").split(" ")
ans =0
for i in a:
    if a in b:
        ans+=1
print(ans)
