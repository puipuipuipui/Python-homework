def solve(data):
    i = 2
    test = True
    while i**2 <= data:
        if data%i ==0:
            test = False
            break
        i+=1
    return test

num1 = int(input("請輸入第一個要判斷的數字："))
num2 = int(input("請輸入第二個要判斷的數字："))
if abs(num1-num2) != 2:
    print("N")
else:
    ans1 = solve(num1)
    ans2 = solve(num2)
    if ans1 and ans2 :
        print("Y")
    else:
        print("N")
