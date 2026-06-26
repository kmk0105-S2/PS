from collections import deque
    
def solution(progresses, speeds):
    q = deque()
    a = 0
    for i in range(len(progresses)):
        work = 0
        a = 100 - progresses[i]
        if a % speeds[i] != 0:
            work = (a // speeds[i]) + 1
        else:
            work = (a // speeds[i])
            
        q.append(work)
    
    tmp = 0
    answer = []
    while(len(q) > 0):
        tmp = q.popleft()
        cnt = 1
        while q and q[0] <= tmp:
            q.popleft()
            cnt += 1
        answer.append(cnt)
    return answer