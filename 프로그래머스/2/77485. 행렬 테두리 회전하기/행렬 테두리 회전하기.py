def change(x1, y1, x2, y2, maps):
    prev = maps[x1][y1]
    minimum = prev
    
    # 위쪽 →
    for y in range(y1+1, y2+1):
        temp = maps[x1][y]
        maps[x1][y] = prev
        prev = temp
        minimum = min(prev, minimum)
    
    # 오른쪽 ↓
    for x in range(x1+1, x2+1):
        temp = maps[x][y2]
        maps[x][y2] = prev
        prev = temp
        minimum = min(prev, minimum)
        
    # 아래쪽 ←
    for y in range(y2-1, y1-1, -1):
        temp = maps[x2][y]
        maps[x2][y] = prev
        prev = temp
        minimum = min(prev, minimum)
    
    # 왼쪽 ↑
    for x in range(x2-1, x1-1, -1):
        temp = maps[x][y1]
        maps[x][y1] = prev
        prev = temp
        minimum = min(minimum, prev)

    return minimum


def solution(rows, columns, queries):
    maps = [[0]*columns for _ in range(rows)]
    
    index = 0
    for i in range(rows):
        for j in range(columns):
            index += 1
            maps[i][j] = index
    
    answer = []

    for line in queries:
        x1 = line[0] - 1
        y1 = line[1] - 1
        x2 = line[2] - 1
        y2 = line[3] - 1
        
        result = change(x1, y1, x2, y2, maps)
        answer.append(result)
    
    return answer