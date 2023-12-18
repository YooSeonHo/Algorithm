import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())

poketmons_keyIsNum = defaultdict(str)
poketmons_keyIsStr = defaultdict(int)

for i in range(1,n+1):
    p = input().rstrip()
    poketmons_keyIsNum[i] = p
    poketmons_keyIsStr[p] = i

for _ in range(m) :
    cmd = input().rstrip()

    if 65<= ord(cmd[0]) <= 90 or 97 <= ord(cmd[-1]) <= 122 :
        print(poketmons_keyIsStr[cmd])
    else :
        print(poketmons_keyIsNum[int(cmd)])