d = [[0 for _ in range(100)] for _ in range(100)]
T = int(input())
result = 0
for i in range(T):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            if d[x+j][y+k] == 0:
                d[x+j][y+k] = 1
for i in range(100):
    for j in range(100):
        if d[i][j] == 1:
            result += 1
print(result)