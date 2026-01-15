from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
def dfs(node):
    visited_dfs[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not visited_dfs[i]:
            dfs(i)

visited_bfs = [False]* (n + 1)
def bfs(node):
    queue = deque([node])
    visited_bfs[node] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)


