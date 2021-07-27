# 스위핑
import sys
N = int(sys.stdin.readline())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
array.sort(key=lambda x:x[0])
now = [array[0][0], array[0][1]]
total = 0
for dot in array[1:]:
    if now[1] >= dot[0]:
        if now[1] < dot[1]:
            now[1] = dot[1]
    else:
        total += now[1] - now[0]
        now = [dot[0], dot[1]]
total += now[1] - now[0]
print(total)