import sys
imput = sys.stdin.readline

n,m = map(int,imput().split())
trees = list(map(int,imput().split()))
left = 0
right = max(trees)
res = 0

while left <= right:
    cnt = 0
    middle = (left + right) // 2
    for tree in trees:
        if tree > middle:
            cnt += (tree - middle)
        if cnt >= m:
            break
    if cnt >= m :
        res = middle
        left = middle +1

    else:
        right = middle -1

print(res)
    


# pypy3로 하면 되는데 python으로 하면 시간초과....
# if cnt>= m : break 추가하면 python으로도 되는데 ㅈㄴ 느리게 댐...