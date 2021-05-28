summ=[2.10, 3.02, 4.39, 4.97, 5.63]
nosumm=[2.10, 2.68, 3.61, 4.01, 4.50]
ele=[120,210,170,200]
n=int(input())
ans1=0
ans2=0
for i in range(len(ele)):
    if n-ele[i]<0:
        ans1+=n*summ[i]
        ans2+=n*nosumm[i]
        break
    else:
        ans1+=ele[i]*summ[i]
        ans2+=ele[i]*nosumm[i]
        n-=ele[i]
print("Summer months:",ans1)
print("Non-Summer months:",ans2)
