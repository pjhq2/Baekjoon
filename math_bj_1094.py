X = int(input())
num = [64, 32, 16, 8, 4, 2, 1]
total = 0
cnt = 0
while total != X:
    for n in num:
        if X >= total + n:
            total += n
            cnt += 1
            break
print(cnt)