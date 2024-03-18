# def solution(name):
#     # 현재 알파벳이 a랑 더 가까운지? z랑 더 가까운지? => 아스키 비교해서 더 작은거 사용 65~90
#     # 커서를 오른쪽으로? 왼쪽으로? => 얘는 어떻게 하지?
#     # => 오른쪽이 A일 떄 두칸 오른쪽으로? 왼쪽으로? 므칭
#     n = len(name)
#     cursor = 0
#     isPlus = True
#     now = ['A'] * n
#     res = 0
    
#     def check_idx(idx) :
#         idx %= n
#         return idx
    
#     def check_alpha(alpha) :
#         if ord(alpha) - 65 > 13 :
#             # A -> Z 로 한번 바꿔줘야 해서 + 1
#             return 90 - ord(alpha) + 1
#         else :
#             return ord(alpha) - 65
            
#     def check_A(cursor) :
#         num = 0
#         for i in range(1,n+1) :
#             if name[(cursor+i)%n] != 'A' :
#                 return num
#             num += 1
#         return num
    
#     while True :
#         print(now)
#         if str(now) == name :
#             return res
        
#         cursor = check_idx(cursor)
        
#         res += check_alpha(now[cursor])
#         now[cursor] = name[cursor]
        
#         # 언제 +? 언제 -? => 다음 커서가 A를 가리킬 때, 현재 위치에서 좌/우 비교
#         # 내 이후에 있는 A의 수와 현재 내 위치를 비교 => 내 이동방향에 A가 cursor + 1 개 이상 있으면 방향 바꿈 
#         # 방향은 애초에 바꾸거나 안바꾸거나 1번만 함
#         if isPlus :
#             a = check_A(cursor)
#             if a >= cursor + 1 :
#                 isPlus = False
#                 res = res + cursor + 1
#                 # 방향 바꿈
#                 cursor = n-1
#             else :
#                 res += 1
#                 cursor += 1
#         else :
#             res += 1
#             cursor -= 1

# solution("JEROEN")

a = ['J', 'E', 'R', 'O', 'E', 'N']
print(''.join(a))