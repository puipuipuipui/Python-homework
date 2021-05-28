a=input("請輸入string_a：")
b=input("請輸入string_b：")
ans=[]
for i in a:
    if (i in b) and not(i in ans):
        ans.append(i)
             
if len(ans) ==0:
    print("N")
else:
    ans.sort()
    print("".join(ans))
