from itertools import combinations


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
mems = [x for x in range(n)]
com = list(combinations(mems,n//2))
res = 10 ** 9

for start_list in com :
    start = 0
    link = 0
    # start_list = list(combinations(p[:n//2],2))
    # link_list = list(combinations(p[n//2:],2))
    # 메모리 = 40 * 19 * 2 * 40! .... 당연히 초과
    
    link_list = list(set(mems) - set(start_list))
    for s in combinations(start_list,2) :
        start += arr[s[0]][s[1]]
        start += arr[s[1]][s[0]]
    for l in combinations(link_list,2) :
        link += arr[l[0]][l[1]]
        link += arr[l[1]][l[0]]


    # for s in start_list :
    #     start += arr[s[0]][s[1]]
    #     start += arr[s[1]][s[0]]
    # for l in link_list :
    #     link += arr[l[0]][l[1]]
    #     link += arr[l[1]][l[0]]

    if abs(start-link) == 0 :
        res = 0
        break
    else :
        res = min(res,abs(start-link))

print(res)


#####################################
########### backTracking ############
#####################################


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
members = [x for x in range(n)]
start = []
link = []
res = 10 ** 9

def backTracking(idx) :
    global res
    if len(start) == n // 2 :
        start_point, link_point = 0,0
        link = list(set(members) - set(start))
        # ex. start = [0,1,2] link=[3,4,5] => 얘네 조합을 만들어서 점수를 내야하는뎅;;
        for i in range(n//2) :
            for j in range(n//2) :
                if i == j :
                    continue
                else :
                    start_point += arr[start[i]][start[j]]
                    link_point += arr[link[i]][link[j]]

        ab = abs(start_point - link_point)
        res = min(res,ab)
        return

    else :
        for i in range(idx,n):
            start.append(i)
            backTracking(i+1)
            start.pop()

backTracking(0)
print(res)