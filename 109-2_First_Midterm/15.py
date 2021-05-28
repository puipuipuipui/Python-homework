data=input("輸入一組四位數字為:")
ans=[]
for i in data:
    num=(int(i)+7)%10
    ans.append(num)
print("輸出加密後的數字為:%d%d%d%d" %(ans[2],ans[3],ans[0],ans[1]))



