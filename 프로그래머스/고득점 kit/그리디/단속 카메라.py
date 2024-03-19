
def solution(routes):
    
    routes.sort()
    # 첫번째 나가는 곳엔 무조건 카메라 설치
    # 이 첫번째 카메라와 겹치는 애들 다 뺌
    # 마찬가지로 남은 애들 중에 두번쨰 카메라가 나가는 곳에 설치
    # 반복...
    res = 1
    cam = routes[0][1]
    
    for r in routes[1:] :
        if r[0] <= cam :
            # 만약 [-20,-15]여서 -15에 설치
            # 그리고 다음 애가 [-18,-16], 끝-시작만 비교? 얘도 같이 찍힘
            # 근데 카메라가 -15에 있다면 안찍힐 거
            # 그래서 최솟값을 카메라에 계쏙 넣어주는 거
            cam = min(cam,r[1])
            continue
        else :
            res += 1
            cam = r[1]
            
    return (res)
    