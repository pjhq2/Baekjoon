# 1463 1로 만들기(S3)
d = [0 for i in range(10 ** 6 + 1)]

def solution(n):
    for i in range(2, n + 1):
        d[i] = d[i - 1] + 1
        if i % 3 == 0:
            d[i] = min(d[i // 3] + 1, d[i])
        if i % 2 == 0:
            d[i] = min(d[i // 2] + 1, d[i])
    return d[n]

N = int(input())
print(solution(N))