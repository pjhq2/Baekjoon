# 색종이 자르지 말고 전체를 놓고 부분적으로 확인하기
white = blue = 0
def solution(i, j, n, array):
    global white # 0
    global blue # 1
    for a in range(n):
        for b in range(n):
            if array[i + a][j + b] != array[i][j]:
                solution(i, j, n//2, array)
                solution(i + n//2, j, n//2, array)
                solution(i, j + n//2, n//2, array)
                solution(i + n//2, j + n//2, n//2, array)
                return
    if array[i][j] == 0:
        white += 1
    if array[i][j] == 1:
        blue += 1
    return

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

solution(0, 0, N, paper)
print(white, blue)
