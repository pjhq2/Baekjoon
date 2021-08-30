# 백준 12852 1로 만들기 2(S1)
from collections import deque

N = int(input())
INF = int(1e9)
dp = [INF] * (N + 1)
dp[1] = 0


def pre_setting(n):
    queue = deque([n])
    while queue:
        n = queue.popleft()
        if n+1 <= N and dp[n+1] > dp[n]+1:
            dp[n+1] = dp[n] + 1
            queue.append(n+1)
        if 2*n <= N and dp[2*n] > dp[n]+1:
            dp[2*n] = dp[n]+1
            queue.append(2*n)
        if 3*n <= N and dp[3*n] > dp[n]+1:
            dp[3*n] = dp[n]+1
            queue.append(3*n)


pre_setting(1)
print(dp[N])

save = [N]
while N > 1:
    if not N % 3 and dp[N//3] == dp[N]-1:
        save.append(N//3)
        N //= 3
    elif not N % 2 and dp[N//2] == dp[N]-1:
        save.append(N//2)
        N //= 2
    elif dp[N-1] == dp[N] - 1:
        save.append(N-1)
        N -= 1

print(*save)