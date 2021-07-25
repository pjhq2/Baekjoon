# 11726 2xn 타일링(S3)
import sys
sys.setrecursionlimit(10000)

n = int(input())
d = [0 for _ in range(n + 1)]

def solution(n):
    if n <= 2:
        d[n] = n
        return d[n]
    if d[n] == 0:
        d[n] = solution(n - 1) + solution(n - 2)
    return d[n]

def divide(x):
    return x % 10007

print(divide(solution(n)))