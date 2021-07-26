import sys

N = int(sys.stdin.readline())
costs = [[0, 0, 0]]
for _ in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))
d = [[0 for _ in range(3)] for _ in range(N+1)]

def solution(n):
    for i in range(3):
        d[1][i] = costs[1][i]

    for n in range(2, N+1):
        for i in range(3):
            d[n][i] = costs[n][i] + min(d[n-1][i-1], d[n-1][i-2]) # R
            d[n][i-1] = costs[n][i-1] + min(d[n-1][i-2], d[n-1][i]) # G
            d[n][i-2] = costs[n][i-2] + min(d[n-1][i], d[n-1][i-1]) # B

    return min(d[n][i], d[n][i-1], d[n][i-2])

print(solution(N))