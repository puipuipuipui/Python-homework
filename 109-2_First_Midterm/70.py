data=input().split(" ")
cha="00 01 100 101 1100 1101 11100 11101 111100 111101".split(" ")
word="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
for i in data:
    ans=ans + str(cha.index(i))
print(word[(int(ans)+2)%26])


