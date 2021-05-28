
data=input("輸入月及日為:").split(" ")
mon=int(data[0])
day=int(data[1])
star=["Aquarius","Pisccs","Aries","Taurus","Gemini","Cancer","Loe","Virgo","Libra","Scorpio","Sagittarius","Capricorn"]
list1=[21,19,21,21,22,22,23,24,24,24,23,22]
pt=mon-1
if day>list1[pt]:
    print(star[pt])
else:
    pt-=1
    if pt==-1:
        pt=11
    print(star[pt])
