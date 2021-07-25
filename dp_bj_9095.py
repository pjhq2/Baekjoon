# 9095 1, 2, 3 더하기(S3)
d = [0] * 12
answer = []
def solution(n):
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    return d[n]
T = int(input())
for _ in range(T):
    N = int(input())
    answer.append(solution(N))
for i in range(T):
    print(answer[i])