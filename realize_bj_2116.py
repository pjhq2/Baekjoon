import sys
# sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
dices = []
for _ in range(N):
    dices.append(list(map(int, sys.stdin.readline().split())))

result = 0
for first_num in range(1, 7):
    num = first_num
    total = 0
    for dice in dices:
        for idx, i in enumerate(dice):
            if num == i:
                if idx == 0:
                    num = dice[5]
                    total += max(dice[1], dice[2], dice[3], dice[4])
                elif idx == 1:
                    num = dice[3]
                    total += max(dice[0], dice[2], dice[4], dice[5])
                elif idx == 2:
                    num = dice[4]
                    total += max(dice[0], dice[1], dice[3], dice[5])
                elif idx == 3:
                    num = dice[1]
                    total += max(dice[0], dice[2], dice[4], dice[5])
                elif idx == 4:
                    num = dice[2]
                    total += max(dice[0], dice[1], dice[3], dice[5])
                elif idx == 5:
                    num = dice[0]
                    total += max(dice[1], dice[2], dice[3], dice[4])
                break
        if total > result:
            result = total

print(result)