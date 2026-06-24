def solution(s):
    stk = []
    for i in range(len(s)):
        stk.append(s[i])
        if len(stk) >= 2 and stk[-2] == '(' and stk[-1] == ')':
            stk.pop()
            stk.pop()
        else:
            continue
    if len(stk) == 0:
        return True
    return False