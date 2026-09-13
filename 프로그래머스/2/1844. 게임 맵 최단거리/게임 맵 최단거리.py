from collections import deque

def bfs(r, c, maps):
    q = deque()
    visited = [[False]*c for _ in range(r)]
    visited[0][0] = True
    q.append((0,0))
    
    while q:
        qr, qc = q.popleft()
        
        if qr == r - 1 and qc == c - 1:
            return maps[qr][qc]
        
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = qr + dr
            nc = qc + dc
            
            if 0<=nr<r and 0<=nc<c and not visited[nr][nc] and maps[nr][nc] == 1:
                visited[nr][nc] = True
                maps[nr][nc] = maps[qr][qc] + 1
                q.append((nr, nc))
                
    return -1


def solution(maps):
    r = len(maps)
    c = len(maps[0])
    
    return bfs(r, c, maps)