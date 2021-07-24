# 1927 최소 힙
import heapq
import sys
h = []
arith = []
N = int(sys.stdin.readline())
for _ in range(N):
    arith.append(int(sys.stdin.readline()))
for a in arith:
    if a != 0:
        heapq.heappush(h, a)
    else:
        if len(h) == 0:
            print(0)
        else:
            x = heapq.heappop(h)
            print(x)