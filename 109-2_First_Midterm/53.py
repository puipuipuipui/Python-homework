data=float(input("請輸入路程公里數(km):"))
ans=75
if data==0:
    print("所需車資為: 0")
else:
    if data>=1.5:
        data-=1.5
        add=int(data//0.25+0.5)
        if data%0.25>0:
            add+=1
        print("所需車資為:",ans+add*5)
    else:
        print("所需車資為: 75")
