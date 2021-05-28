data=input("輸入月租型式及通話時間為:").split(",")
kind=[186,386,586,986]
mon=[0.09, 0.08, 0.07, 0.06]
less=[0.9,0.8,0.7,0.6]
many=[0.8,0.7,0.6,0.5]

pt=kind.index(int(data[0]))
money=int(int(data[1])*mon[pt]+0.5)

if money<=kind[pt]:
    print("通話費為:",kind[pt])
else:
    if money*2>=kind[pt]:
        print("通話費為:",int(money*many[pt]+0.5))
    else:
        print("通話費為:",int(money*less[pt]+0.5))