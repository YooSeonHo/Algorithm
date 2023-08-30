from math import lcm

s = input()
t = input()

if s * len(t) == t * len(s):
    print(1)
else : 
    print(0)



# 다른 풀이 -> 최소 공배수 이용 (위 풀이를 최적화)
LCM = lcm(len(s),len(t))
# 최소 공배수 만큼만 곱해주면 됨
s,t = s * (LCM // len(s)) , t * (LCM // len(t))
print(1 if s == t else 0)