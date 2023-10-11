

n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
res = 0
row = [True] * n
column = [True] * n
# 만약 한 줄이 다 동일하다면 다시 체크하지 않도록

def all_same(arr) :
    global res

    for i in range(n) :
        #행 체크
        if all(x == arr[i][0] for x in arr[i]) :
            row[i] = False
            res += 1

        #열 체크
        col = [a[i] for a in arr]
        if all(x == col[0] for x in col) : 
            column[i] = False
            res += 1
        

def bridge_check(arr) :
    global res,l

    #행부터 체크
    for i in range(n) :
        minus_cnt = 0
        if row[i] :
            com = arr[i][0]
            visited = [False] * n
            for j in range(1,n) :
                if abs(com-arr[i][j]) > 1 :
                    break
                # +1 일 경우 , "나"를 포함한 내 앞에 애들이 l만큼 나랑 같은 크기인지 체크해야함....
                elif com-arr[i][j] == -1 :
                    if minus_cnt :
                        break
                    
                    end = j-1-l
                    bridge = []

                    if end < -1 :
                        break
                    elif end == -1 :
                        bridge = [com == a for a in arr[i][j-1::-1]]
                    else : 
                        bridge = [com == a for a in arr[i][j-1:j-1-l:-1]]

                    if bridge and all(bridge) :
                        if end > -1 :
                            if not any(visited[j-1:j-1-l:-1]) :
                                com = arr[i][j]
                                for k in range(j-1,j-1-l,-1) :
                                    visited[k] = True
                            else : break
                        elif end == -1 :
                            if not any(visited[j-1::-1]) :
                                com = arr[i][j]
                                for k in range(j-1,-1,-1) :
                                    visited[k] = True
                            else : break
                    else :
                        break

                # -1 일 경우
                elif com-arr[i][j] == 1 :
                    minus_cnt += 1
                    if minus_cnt == l and not any(visited[j:j-l:-1]) :
                        for k in range(j,j-l,-1) :
                            visited[k] = True
                        com = arr[i][j]
                        minus_cnt = 0

                if com == arr[i][j] :
                    if minus_cnt > 0 :
                        break

                    if j == n-1 :
                        res += 1
                    else :
                        continue

    #열 체크!!!
    for i in range(n) :
        minus_cnt = 0
        col =[a[i] for a in arr]
        visited = [False] * n
        if column[i] :
            com = col[0]
            for j in range(1,n) :
                if abs(com-col[j]) > 1 :
                    break
                # +1 일 경우
                elif com-col[j] == -1 :
                    if minus_cnt > 0   :
                        break

                    # 인덱싱 다시 해야됨!!! 종료값이 -1 이면 역순이어서 맨 뒤를 취급함 나는 +1해서 0 이 되는 줄 알았는데..
                    # 이 부분부터 다시 보면 됨
                    bridge = []
                    end = j-1-l
                    if end < -1 :
                        break
                    elif end == -1 :
                        bridge = [com == c for c in col[j-1::-1]]
                    else :    
                        bridge = [com == c for c in col[j-1:j-1-l:-1]]

                    if bridge and all(bridge) :
                        if end > -1 :
                            if not any(visited[j-1:j-1-l:-1]) :
                                com = col[j]
                                for k in range(j-1,j-1-l,-1) :
                                    visited[k] = True
                            else : break
                        elif end == -1 :
                            if not any(visited[j-1::-1]) :
                                com = col[j]
                                for k in range(j-1,-1,-1) :
                                    visited[k] = True

                            else : break
                    else :
                        break
                   
                # -1 일 경우
                elif com-col[j] == 1 :
                    minus_cnt += 1
                    if minus_cnt == l and not any(visited[j:j-l:-1]) :
                        for k in range(j,j-l,-1) :
                            visited[k] = True
                        com = col[j]
                        minus_cnt = 0

                if com == col[j] :
                    if minus_cnt > 0 :
                        break

                    if j == n-1 :
                        res += 1
                    else :
                        continue

all_same(arr)
bridge_check(arr)
print(res)