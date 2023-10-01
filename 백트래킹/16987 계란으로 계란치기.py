import sys
input = sys.stdin.readline

n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]
# egg = 내구도, 무게 순
res = []
broken = [0] * n
def backTracking(idx):
    if idx == n: 
        
        cnt = 0 
        for e in eggs :
            if e[0] <= 0 :
                cnt +=1
        res.append(cnt)
        return

    #idx 빼고 모두가 음수일때도 리턴하고 끝내야함..
    #내구도가 0 이하일때도 백트래킹을 불러서, 프루닝되게 해야함

    if eggs[idx][0] <= 0  :
        broken[idx] = 1
        backTracking(idx+1)
        broken[idx] = 0


    else :
       
        if all(broken[:idx]+broken[idx+1:]) :
            backTracking(n)
            
        for i in range(n) :
            
            if i != idx and not broken[i] and  not broken[idx] :
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                if eggs[idx][0] <= 0 :
                    broken[idx] = 1
                if eggs[i][0] <= 0 :
                    broken[i] = 1
                backTracking(idx+1)
                broken[idx] = 0
                broken[i] = 0
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]


                
backTracking(0)
print(max(res))


##########################################################################################
#################### pypy3 ###############################################################
##########################################################################################
import sys
input = sys.stdin.readline

n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]
# egg = 내구도, 무게 순
res = []

def backTracking(idx):
        
    if idx == n: 
        
        cnt = 0 
        for e in eggs :
            if e[0] <= 0 :
                cnt +=1
        res.append(cnt)
        return

    #idx 빼고 모두가 음수일때도 리턴하고 끝내야함..
    #내구도가 0 이하일때도 백트래킹을 불러서, 프루닝되게 해야함
    else :
       
        for i in range(n) :
            if eggs[idx][0] <= 0 or all([e[0] <= 0 for e in eggs[:idx]] + [e[0]<=0 for e in eggs[idx+1:]]):
                backTracking(idx+1)

            elif i != idx and eggs[i][0] > 0 and eggs[idx][0] > 0 :
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                backTracking(idx+1)
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]


                
backTracking(0)
print(max(res))
