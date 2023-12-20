import sys
from collections import defaultdict
input = sys.stdin.readline

keyIsTree = defaultdict(list)

#stdin.readline => 아무것도 입력 못받으면 빈 문자열 반환
idx = 0
while True :
    tree = input().rstrip()
    if not tree :
        break

    keyIsTree[tree].append(idx)
    idx += 1

sortTree = sorted(keyIsTree.items())
for t in sortTree :
    print(t[0],format(len(t[1])/idx * 100,".4f"),sep=' ')