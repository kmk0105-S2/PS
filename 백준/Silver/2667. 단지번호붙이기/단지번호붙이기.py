from collections import deque

n = int(input())

zido = []

for i in range(n):
    line = list(map(int,input().strip()))
    zido.append(line)

visited = [[False]*n for _ in range(n)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if zido[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))
    
    return count

results = []

for i in range(n):
    for j in range(n):
        if zido[i][j] == 1 and not visited[i][j]:
            count = bfs(i, j)
            results.append(count)

print(len(results))

for r in sorted(results):
    print(r)




