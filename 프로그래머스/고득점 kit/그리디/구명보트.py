def solution(people, limit):
    n = len(people)
    res = 0
    people.sort()
    visited = [1] * n
    # 최대한 limit에 가깝게 태워서 보내야함 => 투포인터?
    # [50,50,70,80]
    s,e = 0, n-1
    
    while s < e :
        now = people[s] + people[e]
        if now <= limit :
            visited[s] = visited[e] = 0
            s += 1
            e -= 1
            res += 1
        else :
            visited[e] = 0
            e -= 1
            res += 1

    res += sum(visited)
    return res
    