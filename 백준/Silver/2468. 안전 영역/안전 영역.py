import sys
sys.setrecursionlimit(100000)

n = int(input())

ground = []

ground = [list(map(int, input().split())) for _ in range (n)]

max_h = 0
min_h = 100

for i in range(n):
    for j in range(n):
        if(min_h > ground[i][j]): min_h = ground[i][j]
        if(max_h < ground[i][j]): max_h = ground[i][j]


visited = []

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

def dfs(x, y, rain, visited):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if ground[nx][ny] > rain and not visited[nx][ny]:
                dfs(nx, ny, rain, visited)

max_area = 1
for rain in range(min_h, max_h):
    visited = [[False]*n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if ground[i][j] > rain and not visited[i][j]:
                dfs(i, j, rain, visited)
                count += 1
    max_area = max(max_area, count)

print(max_area)
                