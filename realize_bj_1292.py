series = []
i = 0
cnt = 0
# 수열 구현
while cnt < 1000:
    i += 1
    for _ in range(i):
        series.append(i)
        cnt += 1
        if cnt >= 1000:
            break
A, B = list(map(int, input().split()))
print(sum(series[A-1:B]))