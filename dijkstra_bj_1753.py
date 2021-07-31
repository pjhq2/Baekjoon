import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost)) # (대상 정점, 가중치)

def dijkstra(K):
    distance[K] = 0
    q = []
    heapq.heappush(q, (0, K)) # (가중치, 정점)
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])