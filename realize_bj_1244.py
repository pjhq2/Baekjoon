# 입력 받기
N = int(input())
switch = [0]
switch.extend(map(int, input().split()))
student_number = int(input())
students = []
for _ in range(student_number):
    students.append(list(map(int, input().split())))

# 리턴 값 없는 스위치 체인저
def switch_change(switch, gender, number):
    if gender == 1:
        for i in range(number, N+1, number):
            if switch[i] == 0:
                switch[i] = 1
            elif switch[i] == 1:
                switch[i] = 0

    elif gender == 2:
        if switch[number] == 0:
            switch[number] = 1
        elif switch[number] == 1:
            switch[number] = 0
        i = 1
        while True:
            if 1 <= number-i <= N and 0 <= number+i <= N and switch[number-i] == switch[number+i]:
                if switch[number-i] == 0:
                    switch[number-i] = switch[number+i] = 1
                elif switch[number-i] == 1:
                    switch[number-i] = switch[number+i] = 0
                i += 1
            else:
                break

# 계산 및 출력
for i in range(student_number):
    switch_change(switch, students[i][0], students[i][1])
for i in range(5):
    try:
        print(' '.join(map(str, switch[1+20*i:21+20*i])))
    except:
        break