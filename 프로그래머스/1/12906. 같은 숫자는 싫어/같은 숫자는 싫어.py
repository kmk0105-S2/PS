def solution(arr):
    stk = []
    stk.append(arr[0])
    top = 0
    for i in range(1, len(arr)):
        stk.append(arr[i])
        top += 1
        if (stk[top] == stk[top - 1]):
            stk.pop()
            top -= 1
        
    return stk