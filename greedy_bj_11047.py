# 그리디로 푸는게 동적 프로그래밍보다 빠른 경우라고 함
N, K = map(int, input().split())
value = []
for i in range(N):
    value.append(int(input()))
value.sort(reverse=True)
result = 0
rest = K
for i in value:
    if rest >= i:
        result += rest // i
        rest = rest % i
    if rest == 0:
        break
print(result)