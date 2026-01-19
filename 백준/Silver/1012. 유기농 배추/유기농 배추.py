from collections import deque

t = int(input())
jido = []
visited = []

for i in range (t):
    m, n, k = map(int, input().split())
    jido = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    result = 0

    for j in range(k):
        x, y = map(int, input().split())
        jido[y][x] = 1

    def bfs(y, x):
        queue = deque([(y, x)])
        visited[y][x] = True
        count = 1

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        while queue:
            cy, cx = queue.popleft()

            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if 0 <= nx < m and 0<= ny <n:
                    if jido[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny, nx))

    
    for q in range(n):
        for p in range(m):
            if jido[q][p] == 1 and not visited[q][p]:
                bfs(q, p)
                result += 1
    print(result)
