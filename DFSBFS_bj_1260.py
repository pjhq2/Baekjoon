from collections import deque

N, M, V = list(map(int, input().split()))
graph = []
zido = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
dfs_result = []
bfs_result = []

for _ in range(M):
    temp = sorted(list(map(int, input().split())))
    zido[temp[0]].append(temp[1])
    zido[temp[1]].append(temp[0])
for i in range(N+1):
    if len(zido[i]) != 0:
        zido[i].sort()

def dfs(zido, v, visited_dfs):
    visited_dfs[v] = True
    dfs_result.append(str(v))
    for x in zido[v]:
        if visited_dfs[x] == False:
            dfs(zido, x, visited_dfs)

def bfs(zido, v, visited_bfs):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        result = queue.popleft()
        bfs_result.append(str(result))
        for i in zido[result]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(zido, V, visited_dfs)
print(' '.join(dfs_result))
bfs(zido, V, visited_bfs)
print(' '.join(bfs_result))