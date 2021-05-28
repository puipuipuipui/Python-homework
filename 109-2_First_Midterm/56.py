
data=input("請選擇主餐及升級的套餐：")
ans=0
if input("是否升級成大杯飲料：")=="是":
    ans+=7
if input("是否換成大薯：")=="是":
    ans+=13    
food=[72,62,82,44,60]
ans+=food[int(data[0])-1]
if data[1]=="A":
    ans+=55
else:
    ans+=68

print("總共為",ans,"元")
