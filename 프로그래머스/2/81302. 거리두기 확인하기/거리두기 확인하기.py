from collections import deque

def bfs(room, sr, sc):
    q = deque()
    q.append((sr, sc, 0))
    visited = [[False]*5 for _ in range(5)]
    visited[sr][sc] = True
    
    while q:
        r, c, dist = q.popleft()
        
        if dist == 2:
            continue
        
        for dr, dc in [(-1, 0), (1,0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc]:
                if room[nr][nc] == 'X':
                    continue
                if room[nr][nc] == 'P':
                    return False
                visited[nr][nc] = True
                q.append((nr, nc, dist+1))
                
    return True
    
def solution(places):
    result = []
    room = []
    for i in range(5):
        room = places[i]
        ok = True
        for r in range(5):
            for c in range(5):
                if room[r][c] == 'P':
                    if not bfs(room, r, c):
                        ok = False
                        break
            if not ok:
                break
        result.append(1 if ok else 0)
        
    return result 
        