bingo = [list(map(int, input().split())) for _ in range(5)]
result = [[0] * 5 for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]


def bingo_num(result):
    total = 0
    # 가로
    for i in range(5):
        if sum(result[i]) == 5:
            total += 1
    # 대각
    temp1 = temp2 = 0
    for i in range(5):
        if result[i][i] == 1:
            temp1 += 1
        if temp1 == 5:
            total += 1
        if result[4-i][i] == 1:
            temp2 += 1
        if temp2 == 5:
            total += 1
    # 세로
    result = list(zip(*result))
    for i in range(5):
        if sum(result[i]) == 5:
            total += 1

    return total


def bingo_do(bingo, result, numbers):
    for i in range(5):
        for j in range(5):
            for x in range(5):
                for y in range(5):
                    if bingo[y][x] == numbers[i][j]:
                        result[y][x] = 1
                        if bingo_num(result) >= 3:
                            return 5 * i + (j + 1)


print(bingo_do(bingo, result, numbers))
