import sys
sys.stdin = open('input.txt')

n = int(input())
mines = [input() for _ in range(n)]
opens = [input() for _ in range(n)]
result = [[] for _ in range(n)]
lose = False

for i in range(n):
    for j in range(n):
        if opens[i][j] == 'x':  # 열린 칸일 때
            if mines[i][j] == '.':  # 지뢰가 없다면
                cnt = 0
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        if 0 <= i+p < n and 0 <= j+q < n and mines[i+p][j+q] == '*' and not (p == 0 and q == 0):
                            cnt += 1
                result[i].append(str(cnt))
            else:
                lose = True
                result[i].append('*')
        else:
            result[i].append('.')

if lose:
    for i in range(n):
        for j in range(n):
            if mines[i][j] == '*':
                result[i][j] = '*'

for i in range(n):
    print(''.join(result[i]))
