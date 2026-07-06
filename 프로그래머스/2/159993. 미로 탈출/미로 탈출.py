from collections import deque

def bfs(start, end, maps):
    visited = [[False]*(len(maps[0])) for _ in range(len(maps))]
    flag = False
    q = deque()
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:
                q.append((i, j, 0))
                visited[i][j] = True
                break
                
    while q:
        r, c, time = q.popleft()
        
        if maps[r][c] == end:
            return time
        
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            mr = r+ dr
            mc = c + dc
            
            if 0<=mr<len(maps) and 0<=mc<len(maps[0]) and maps[mr][mc] != 'X':
                if not visited[mr][mc]:
                    visited[mr][mc] = True
                    q.append((mr, mc, time+1))
                    
    return -1

def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)
    
    if path1 != -1 and path2 != -1:
        return path1 + path2
    
    else:
        return -1
                