def solution(arr):
    stk = []
    i = 0
    index = -1
    while(i < len(arr)):
        if (index == -1):
            stk.append(arr[i])
            i += 1
            index += 1
        else:
            if (stk[index] < arr[i]):
                stk.append(arr[i])
                i += 1
                index += 1
            else:
                stk.pop()
                index -= 1
    
    return stk