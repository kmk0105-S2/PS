def solution(board, moves):
    stk = []
    result = 0
    for i in range(len(moves)):
        index = moves[i] - 1
        tmp = 0
        for j in range(len(board)):
            if (board[j][index] == 0):
                continue
            else:
                tmp = board[j][index]
                board[j][index] = 0
                stk.append(tmp)
                break
        if len(stk) >= 2 and stk[-2] == stk[-1]:
            stk.pop()
            stk.pop()
            result += 2
    return result