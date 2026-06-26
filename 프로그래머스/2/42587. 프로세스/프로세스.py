from collections import deque

def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    
    count = 0
    while q:
        max_p = max(p for i, p in q)
        i, p = q.popleft()
        if p < max_p:
            q.append((i, p))
        else:
            count += 1
            if i == location:
                return count
        