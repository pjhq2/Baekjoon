# 끝나는 시간이 제일 적은 것 골라
# 끝나는시간부터 끝나는시간이 제일 적은거 골라
# 정렬 2번!
N = int(input())
conv = []
for i in range(N):
    conv.append(list(map(int, input().split())))
conv.sort(key=lambda a: a[0])
conv.sort(key=lambda a: a[1])
cnt = 0
temp = conv[0][0]
for i in conv:
    if temp <= i[0]:
        cnt += 1
        temp = i[1]
print(cnt)