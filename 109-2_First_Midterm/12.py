data=input("輸入一整數序列為:").split(" ")
setdata=set(data)
test=True
for i in setdata:     
    if data.count(i) >= len(data)/2:
        print("過半元素為:",i)
        test=False
        break
if test:
    print("過半元素為:","NO")
