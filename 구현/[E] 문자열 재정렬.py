s = input()
alpha = []
num = []

for i in s :
    if ord(i)>=65 and ord(i) <=90 :
        alpha.append(i)
    else :
        num.append(i)

alpha.sort()
for i in alpha :
    print(i,end='')

if len(num) != 0 :
    print(sum(map(int,num)))
#num이 있는 지 아닌 지 체크 해야함 꼭!