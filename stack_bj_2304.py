N = int(input())

LH = []
for _ in range(N):
    LH.append(list(map(int, input().split())))

LH.sort(key=lambda x: x[1], reverse=True)

h = LH[0][1]
start = LH[0][0]
end = LH[0][0] + 1

total = h
for lh in LH:  # 굳이 for문 안쓰고 stack에서 하나씩 빼는 방식으로도 구현할 수 있을듯!
    if lh[0] < start:
        total += lh[1] * (start - lh[0])
        start = lh[0]
    elif lh[0] >= end:
        total += lh[1] * (lh[0]+1 - end)
        end = lh[0]+1

print(total)