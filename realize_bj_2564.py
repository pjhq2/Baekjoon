import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]
dong = list(map(int, input().split()))

total = 0
if dong[0] == 1:  # 북쪽
    for store in stores:
        if store[0] == dong[0]:  # 같은 선상일 때 걍 계산
            total += abs(dong[1] - store[1])
        elif store[0] == 3:  # 서쪽
            total += dong[1] + store[1]
        elif store[0] == 4:  # 동쪽
            total += w-dong[1] + store[1]
        else:  # 남쪽
            total += min(dong[1] + h + store[1], w-dong[1] + h + w-store[1])

elif dong[0] == 2:  # 남쪽
    for store in stores:
        if store[0] == dong[0]:  # 같은 선상일 때 걍 계산
            total += abs(dong[1] - store[1])
        elif store[0] == 3:  # 서쪽
            total += dong[1] + h-store[1]
        elif store[0] == 4:  # 동쪽
            total += w - dong[1] + h-store[1]
        else:  # 북쪽
            total += min(dong[1] + h + store[1], w - dong[1] + h + w - store[1])

elif dong[0] == 3:  # 서쪽
    for store in stores:
        if store[0] == dong[0]:  # 같은 선상일 때 걍 계산
            total += abs(dong[1] - store[1])
        elif store[0] == 1:  # 북쪽
            total += dong[1] + store[1]
        elif store[0] == 2:  # 남쪽
            total += h-dong[1] + store[1]
        else:  # 동쪽
            total += min(dong[1] + w + store[1], h-dong[1] + w + h-store[1])

elif dong[0] == 4:  # 동쪽
    for store in stores:
        if store[0] == dong[0]:  # 같은 선상일 때 걍 계산
            total += abs(dong[1] - store[1])
        elif store[0] == 1:  # 북쪽
            total += dong[1] + w - store[1]
        elif store[0] == 2:  # 남쪽
            total += h - dong[1] + w - store[1]
        else:  # 서쪽
            total += min(dong[1] + w + store[1], h - dong[1] + w + h - store[1])

print(total)