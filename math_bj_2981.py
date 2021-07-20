# Python3로는 시간 초과, PyPy3로 돌리면 시간 초과 안뜸
# 유클리드 호제법을 활용해서 풀어야 시간이 절약되고 시간 초과 안뜸
# 수학적 지식이 필요한 문제
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, (a % b)
    return a

N = int(input())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
num.sort()

M_max = num[1] - num[0]
for i in range(2, N):
    M_max = gcd(M_max, num[i]-num[i-1])

result = []
for i in range(2, M_max//2 + 1):
    if M_max % i == 0:
        result.append(str(i))
result.append(str(M_max))
print(' '.join(result))