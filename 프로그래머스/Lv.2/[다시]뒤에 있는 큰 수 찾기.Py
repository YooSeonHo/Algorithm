


def solution(numbers):
    n = len(numbers)
    stack = []
    answer = [-1] * n
    
    for i in range(n) :
        while stack and numbers[stack[-1]] < numbers[i] :
            answer[stack.pop()] = numbers[i]
        stack.append(i)
        
    return answer


# 100만개 => 이중 포문으로 돌리면 반드시 시간초과
# 그렇다면 우선 순위 큐 ? => 인덱스를 저장할 방법이 없다....
# 그냥 스택 + 인덱스를 활용해서 해야함!
# 스택에 아무 것도 없거나, 현재 인덱스보다 작은 인덱스 중 작은 수가 없다면 그냥 스택에 추가
# 나보다 작은 수를 가진 인덱스가 있다면 답에 내 수를 적어주고, 스택에서 팝

