N = int(input())
money_time = list(map(int, input().split()))
money_time.sort()
sum = 0
for i in range(N):
    sum += money_time[i] * (N - i)
print(sum)