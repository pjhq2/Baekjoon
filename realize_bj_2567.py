# 구석에 있는 요소가 1번만 계산되서 문제 발생했었음, 디버깅의 중요성!
d = [[0 for _ in range(102)] for _ in range(102)]
T = int(input())
result = 0
for i in range(T):
    x, y = map(int, input().split())
    for j in range(1, 11):
        for k in range(1, 11):
            if d[x+j][y+k] == 0:
                d[x+j][y+k] = 1
for i in range(101):
    for j in range(101):
        if (d[i][j] == 0 and d[i+1][j] == 1):
            result += 1
        if (d[i][j] == 1 and d[i+1][j] == 0):
            result += 1
        if (d[i][j] == 0 and d[i][j+1] == 1):
            result += 1
        if (d[i][j] == 1 and d[i][j+1] == 0):
            result += 1
print(result)