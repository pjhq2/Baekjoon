# 11286 절댓값 힙
# 우선 순위 큐(힙에 (우선 순위, 작업) 형태로 저장)
import heapq
import sys
h = []
arith = []
N = int(sys.stdin.readline())
for _ in range(N):
    arith.append(int(sys.stdin.readline()))
for a in arith:
    if a != 0:
            heapq.heappush(h, (abs(a), a))
    else:
        if len(h) == 0:
            print(0)
        else:
            x = heapq.heappop(h)
            print(x[1])