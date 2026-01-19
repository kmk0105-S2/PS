from collections import deque

n, m = map(int, input().split())
jido =[list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
dap = 0

for i in range(n):
    for j in range(m):
        if jido[i][j] == 0:
            empty.append((i, j))
        if jido[i][j] == 2:
            virus.append((i, j))

def bfs():
    temp_jido = [line[:] for line in jido]
    queue = deque(virus)
    safe_count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx <n and 0<= ny <m:
                if temp_jido[nx][ny] == 0:
                    temp_jido[nx][ny] = 2
                    queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if temp_jido[i][j] == 0:
                safe_count += 1

    return safe_count

def select_walls(start, cnt):
    global dap
    if cnt == 3 :
        dap = max(dap, bfs())
        return
    
    for i in range(start, len(empty)):
        r, c = empty[i]

        jido[r][c] = 1
        select_walls(i + 1, cnt + 1)
        jido[r][c] = 0

select_walls(0, 0)
print(dap)