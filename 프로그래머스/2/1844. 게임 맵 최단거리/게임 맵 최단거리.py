from collections import deque

def bfs(maps, r, c, n, m):
    q = deque()
    q.append((r, c, 1))
    visited = [[False]*m for _ in range(n)]
    visited[r][c] = True
    
    while q:
        r, c, dist = q.popleft()
        
        if r == n -1 and c == m - 1:
            return dist
        
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = dr + r
            nc = dc + c
            
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                if maps[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc, dist+1))

    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    return bfs(maps, 0, 0, n, m)
    
    
    
        
    