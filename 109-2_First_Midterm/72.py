def count(n,k,ans):
    if n<k:
        return ans
    else:    
        num=n//k
        r=n%k+num
        ans+=num
        return count(r, k, ans)

n=int(input("請輸入n:"))
k=int(input("請輸入k:"))
print("Peter可以抽%d支紙菸" %(count(n,k,n)))
