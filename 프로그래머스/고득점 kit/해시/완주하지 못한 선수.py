def solution(participant, completion):
    participant.sort()
    completion.sort()
    n = len(completion)
    for i in range(n) :
        if completion[i] != participant[i] :
            return participant[i]
    
    return participant[-1]

#배열이 두개일 때, for문 한 개로 비교하는 방법