# s = (list(input().rstrip()))
# res = 0
# stack = []

# # stack에 담아서 만약 쌍이 맞으면 pop을 하고, 팝했을 때 스택을 검사해서 곱하기를 해버린당

# for i in range(len(s)):
#     print(stack)
#     if i == 0 :
#         stack.append(s[i])
#     else :
#         if len(stack) != 0 :
#              if s[i] == ')' :
#                 if stack[-1] == '(' :
#                     stack.pop()
#                     if len(stack) != 0:
#                         mul = 1
#                         for j in range(len(stack)):
#                             if stack[j] == '(' : 
#                                 mul *= 2
#                             elif stack[j] == '[' :
#                                 mul *= 3
#                         res += mul * 2

#                     else :
#                         res += 2
#                 else :
#                     stack.append(s[i])

#              elif s[i] == ']' :
#                 if stack[-1] == '[' :
#                     stack.pop()
#                     if len(stack) != 0:
#                         mul = 1
#                         for j in range(len(stack)):
#                             if stack[j] == '(' : 
#                                 mul *= 2
#                             elif stack[j] == '[' :
#                                 mul *= 3
                            
#                         res += mul * 3

#                     else :
#                         res += 3
#                 else :
#                     stack.append(s[i])

#              else :
#                 stack.append(s[i])
#         else :
#             stack.append(s[i])

# print(res)

                    

s = list(input().rstrip())
tmp = 1
res = 0
stack = []

for i in range(len(s)):
    if s[i] == '(' :
        stack.append(s[i])
        tmp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        tmp *= 3

    elif s[i] == ')' :
        if not stack or stack[-1] != '(':
            res = 0
            break
        if s[i-1] == '(' :
            res += tmp
            # 왜 s[i-1]을 검사하는지? -> 만약 ([]) 에서 마지막 )를 만났을 경우,
            # 이미 안쪽 []에서 6을 더했으므로, 바깥에 있는 ()는 아무것도 덥하면 안됨! 그래서 체크하는거!
        tmp //= 2
        stack.pop()
    elif s[i] == ']':
        if not stack or stack[-1] != '[' :
            res = 0
            break
        if s[i-1] =='[' :
            res += tmp
        tmp //=3
        stack.pop()

if stack :
    print(0)
else:
    print(res)