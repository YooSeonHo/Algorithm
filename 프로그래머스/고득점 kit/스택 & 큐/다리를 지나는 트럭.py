from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    now_size = 0
    fin = []

    time = 0
    while len(fin) < len(truck_weights) :
        time += 1
        if q:
            now = q.popleft()

        bridgeOut = bridge.popleft()
        
        if bridgeOut :
            fin.append(bridgeOut)
            bridge.append(0)
            now_size -= bridgeOut
        else :
            bridge.append(bridgeOut)
        
        if now_size + now <= weight :
            bridge[-1] = now
            now_size += now
        else :
            q.appendleft(now)
        
    return (time)
        
        
