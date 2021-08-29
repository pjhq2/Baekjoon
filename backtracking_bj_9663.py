N = int(input())


def find_queen(i, matrix):
    global result
    if i == N:
        result += 1  # N까지 무사히 도달했다면 성공
        return

    for j in range(N):
        if i+j not in queen_position_1 and i-j not in queen_position_2 and j not in queen_position_3:
            queen_position_1[i+j] = 1
            queen_position_2[i-j] = 1
            queen_position_3[j] = 1
            matrix[i][j] = 1

            find_queen(i+1, matrix)

            queen_position_1.pop(i+j)
            queen_position_2.pop(i-j)
            queen_position_3.pop(j)
            matrix[i][j] = 0


matrix = [[0] * N for _ in range(N)]
queen_position_1 = {}  # 대각_1
queen_position_2 = {}  # 대각_2
queen_position_3 = {}  # 세로
result = 0
find_queen(0, matrix)
print(result)
