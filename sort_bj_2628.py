x, y = map(int, input().split())
row = [0, x]
col = [0, y]

cut_num = int(input())
for i in range(cut_num):
    axis, num = map(int, input().split())
    if axis == 1:  # 가로로 자르기
        row.append(num)
    elif axis == 0:  # 세로로 자르기
        col.append(num)
row.sort()
col.sort()

new_row = []
new_col = []
for i in range(1, len(row)):
    new_row.append(row[i] - row[i-1])
for i in range(1, len(col)):
    new_col.append(col[i] - col[i-1])
new_row.sort(reverse=True)
new_col.sort(reverse=True)

print(new_row[0]*new_col[0])