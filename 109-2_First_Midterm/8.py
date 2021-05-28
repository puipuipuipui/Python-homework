m=input("輸入第一行正整數為:")
data=input("第二行中數列中的數字為:").split(" ")
num=[]
for i in range(1,int(m)+1):
    num.append(data.count(str(i)))
maxx=max(num)
if maxx==1:
    print("每個數字剛好只出現1次")
else:
    print("最大出現次數的數字為:",num.index(maxx)+1)
    print("出現次數為:",maxx)
