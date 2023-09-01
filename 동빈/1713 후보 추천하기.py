n = int(input())
m = int(input())

case = []
students = [0] * 101
vote = list(map(int,input().split()))

for i in range(m):
    #빈 틀이 있는지 체크
    if len(case) < n :
        if students[vote[i]] == 0 :
            students[vote[i]] += 1
            case.append((vote[i],i,1))
            #몇번쨰로 등록됐는지 i로 표시
        else :
            students[vote[i]] += 1
    else : 
    #빈 틀이 없으면 추천 수 비교 -> 같으면 게시된 시간도 비교해서 삭제 (추천횟수 0으로)
        if students[vote[i]] == 0 :
            
            case.sort(key=lambda x : (x[2],-x[1]))  
            s = case.pop()

            students[s[0]] = 0
            case.append((vote[i],i,1))

        students[vote[i]] += 1
            
case.sort(key= lambda x: x[0])

for i in range(len(case)):
    print(case[i][0],end=' ')