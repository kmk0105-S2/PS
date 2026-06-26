from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0]*bridge_length)
    cnt = 0
    brd_weight = 0
    truck_weights = deque(truck_weights)
    
    while truck_weights or brd_weight > 0:
        cnt += 1
        brd_weight -= q.popleft()
        
        if truck_weights:
            if brd_weight + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                brd_weight += t
                q.append(t)
            else:
                q.append(0)
                
    return cnt