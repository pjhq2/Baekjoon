# 시간 초과를 해결하기 위해 N//n, n//3을 사용하여 최소한 필요한 연산만 수행
# 이외에 다른 방법도 많이 있음
N = int(input())
result = [['*' for _ in range(N)] for _ in range(N)]

def star(n, result):
    if n >= 3:
        for x in range(n//3, 2 * (n//3)):
            for y in range(n // 3, 2 * (n//3)):
                for i in range(N//n):
                    for j in range(N//n):
                        result[x + i*n][y + j*n] = ' '
        star(n//3, result)

star(N, result)
for i in result:
    print(''.join(i))