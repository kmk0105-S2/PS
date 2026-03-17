n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

#북 동 남 서 순서 맞춰서 돌리기
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    #청소하기
    if room[r][c] == 0:
        room[r][c] = 2
        count += 1
    
    #빈 칸 찾기
    found = False

    for _ in range(4):
        d = (d + 3) % 4 #반시계 방향 90도 회전
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
            r, c = nr, nc
            found = True
            break

    if not found:
        br, bc = r - dr[d], c - dc[d]
        if 0 <= br < n and 0 <= bc < m and room[br][bc] != 1:
            r, c = br, bc
        else:
            break

    
print(count)
            
