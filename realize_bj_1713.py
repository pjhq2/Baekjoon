# 문제 조건 착각해서 좀 더 어렵게 풀다가 바꿈
# 첫 설계가 중요하고, 시퀀스형 데이터를 다룰 때 내가 필요한 것이 무엇인가에 대해 확실히하고 가야함
N = int(input()) # 사진틀 개수
b_total = int(input()) # 추천 총 횟수
b_num = list(map(int, input().split())) # 추천받은 학생 번호 나열

picture = [0] * N # 사진틀 N개(1~20) 안에 학생 번호 들어가 있을 것
picture_status = [[0, 0] for _ in range(N)] # 0번은 사진틀 추천, 1번은 사진틀 시간
student = [0] * 101 # 학생 최대 100명(+1)의 추천 수

# 먼저 추천수를 확인하고 그 다음에 오래된 순서를 확인해야함
for i in b_num:
    student[i] += 1 # b_num 중에 i인 학생 추천 +1 (나중에 사진틀에서 사라지면 초기화할 것)
    overlap = 0 # 중복 0 표시
    empty = 0 # 비어있음 0 표시
    #change = 0 # 교체 0 표시
    
    # 사진틀 비어있거나 중복 학생일 경우
    for j in range(N): # 사진틀 1부터 N까지 확인하면서
        if picture[j] == 0: # 빈 사진틀 발견하면
            picture[j] = i # 거기에 i번째 학생 넣기
            picture_status[j][0] = student[i] # 추천 수 업데이트
            picture_status[j][1] = 0 # 사진틀 시간 갱신
            empty = 1
        if picture[j] == i: # 중복된 학생 발견하면
            picture_status[j][0] = student[i] # 추천 수 업데이트
            #picture_status[j][1] += 1  # 사진틀 시간 업데이트
            overlap = 1
            break
            
    # 빈 사진틀 없고 중복 학생도 아닌 경우
    if empty == 0 and overlap == 0:
        # 최소 추천 및 최대 시간인 것 찾기(1개면 됨)
        b_min = 1000
        t_max = 0
        change_index = 0
        for idx, x in enumerate(picture_status):
            if x[0] < b_min:
                b_min = x[0]
                t_max = x[1]
                change_index = idx
                #change = 1
            elif x[0] == b_min: # 추천 수 같을 때 시간으로 넘김
                if x[1] > t_max: # 사진틀에 있는 시간이 더 클 때
                    t_max = x[1]
                    change_index = idx
                    #change = 1

        #if change == 1:
        student[picture[change_index]] = 0 # 교체 학생 추천 초기화
        picture[change_index] = i
        picture_status[change_index][0] = student[i] # 사진틀 추천 갱신
        picture_status[change_index][1] = 0 # 해당 사진틀 시간 초기화

    # 사진 시간, 추천 갱신 ( 아무일도 없는 사진틀도 시간은 갱신되야함 ) -> 시간은 한번에 갱신하자
    for j in range(N):
        if picture[j] != 0:
            picture_status[j][1] += 1

picture.sort()
result = []
for i in picture:
    if i != 0:
        result.append(str(i))
print(' '.join(result))