n=int(input("請輸入一個正整數(<10)："))

for i in range(1,n+1):
    for j in range(1,i+1):
        ans=i*j
        print("%2d" %ans,end=" ")
    print()

