n=input("請輸入正整數:")
prime=[2]
for i in range(3,int(n)+1):
    test=True
    for j in range(len(prime)):
        if i%prime[j]==0:
            test=False
            break
        if (prime[j]**2)>i:
            break
    if test:
        prime.append(i)

list1=[]
for i in range(len(n)):
    for j in range(i,len(n)):
        data=n[i:j+1]
        if int(data) in prime:
            list1.append(int(data))
q=len(list1)
if len(list1)==0:
    print("No prime found")
else:
    print("子字串中最大的質數值為:",max(list1))
