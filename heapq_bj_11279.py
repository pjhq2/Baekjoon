# 11279 최대 힙
import heapq
h = []
arith = []
N = int(input())
for _ in range(N):
    arith.append(int(input()))
for a in arith:
    if a != 0:
        heapq.heappush(h, -a)
    else:
        if len(h) == 0:
            print(0)
        else:
            x = heapq.heappop(h)
            print(-x)