import sys

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()

# 산술평균
print(round(sum(numbers)/len(numbers)))
# 중앙값
print(numbers[len(numbers)//2])
# 최빈값
mode = {}
mode_list = []
for number in numbers:
    if number in mode:
        mode[number] += 1
    else:
        mode[number] = 1
for key, value in mode.items():
    if value == max(mode.values()):
        mode_list.append(int(key))
mode_list.sort()
if len(mode_list) > 1:
    print(mode_list[1])
else:
    print(mode_list[0])
# 범위
if len(numbers) > 1:
    print(max(numbers) - min(numbers))
else:
    print(0)