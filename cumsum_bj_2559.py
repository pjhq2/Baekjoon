# K가 엄청 크면 시간복잡도가 매우 커진다 -> 처음 한번만 K에 대해 계산하기
N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

result = temp = sum(temperatures[:K])
for i in range(K, len(temperatures)):
    temp += temperatures[i] - temperatures[i-K]
    if temp > result:
        result = temp

print(result)