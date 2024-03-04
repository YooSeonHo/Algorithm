def solution(participant, completion):
    participant.sort()
    completion.sort()
    n = len(completion)
    for i in range(n) :
        if completion[i] != participant[i] :
            return participant[i]
    
    return participant[-1]