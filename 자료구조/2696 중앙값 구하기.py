import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    #출력해야 할 숫자 개수
    resNum = (n+1)//2
    nums = []
    res = []
    for _ in range((n//10)+1) :
        li = list(map(int,input().split()))
        nums += li

    res.append(nums[0])

    for i in range(0,int(n/2) * 2,2) :
        tmp = sorted(nums[0:i+3])
        res.append(tmp[len(tmp)//2])

    print(resNum)
    for i in range((resNum//10)+1) :
        print(*res[i*10:i*10+10],end='\n')
