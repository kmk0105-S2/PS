import sys

input = sys.stdin.readline
n , m , B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

counts = [0]*257
min_h = 256
max_h = 0

for row in range(n):
    for col in range(m):
        h = land[row][col]
        counts[h] += 1
        if h < min_h: min_h = h
        if h > max_h: max_h = h

min_time = sys.maxsize
height = 0

for target in range(min_h, max_h + 1):
    remove = 0
    add = 0

    for h in range(min_h, max_h + 1):
        if counts[h] == 0: continue
        
        if h > target:
            remove += (h - target) * counts[h]
        elif h < target:
            add += (target - h) * counts[h]
    
    if remove + B >= add:
        time = remove * 2 + add

        if time <= min_time:
            min_time = time
            height = target

print(min_time, height)


