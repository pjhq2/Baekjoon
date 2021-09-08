# 백준 3273 두 수의 합(S3)
n = int(input())
series = {}
for i in list(map(int, input().split())):
    if i in series:
        series[i] += 1
    else:
        series[i] = 1
x = int(input())
result = 0
for k, v in series.items():
    if x-k in series:
        result += series[x-k]
print(result//2)