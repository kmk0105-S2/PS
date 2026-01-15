import sys
from collections import deque

# 1. 입력 속도 최적화 및 N, M 받기
input = sys.stdin.readline
n, m = map(int, input().split())

# 2. 미로 입력 받기 (공백 없는 문자열 처리)
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))

# 3. BFS 함수 정의
def bfs(x, y):
    queue = deque([(x, y)])
    
    # 상, 하, 좌, 우 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        # 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위를 벗어나지 않는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                # '1'인 경우만 이동 (길이면서 아직 방문 안 한 곳)
                if maze[nx][ny] == 1:
                    # 현재 위치까지의 거리 = 이전 위치까지의 거리 + 1
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
                    
    # 도착 지점(N, M)의 최단 거리 반환
    return maze[n-1][m-1]

# (0, 0)에서 출발
print(bfs(0, 0))