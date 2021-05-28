n,m=input("輸入N及M為:").split(" ")
data=[]
for i in range(int(n)):    
    data.append(input("輸入矩陣值第"+str(i+1)+"列為:").split(" "))
for i in range(int(m)):
    for j in range(int(n)):
        print(data[j][i],end=" ")
    print()

