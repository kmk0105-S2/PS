def solution(s):
    stk = []
    cnt = 0
    for i in s.split():
        if i == 'Z':
            cnt -= stk.pop()
        else:
            stk.append(int(i))
            cnt += int(i)
        
    return cnt