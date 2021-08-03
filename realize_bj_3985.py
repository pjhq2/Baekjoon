L = int(input())
N = int(input())
cake_ranges = []
cake_amount = [0 for _ in range(L+1)]
result = {}
hope_max = 0
hope_idx = 0
for _ in range(N):
    cake_ranges.append(list(map(int, input().split())))
# 가장 많이 먹을 것으로 예상되는 사람 찾기
for idx, cake_range in enumerate(cake_ranges, start=1):
    if hope_max < cake_range[1] - cake_range[0] + 1:
        hope_max = cake_range[1] - cake_range[0] + 1
        hope_idx = idx
    # 케이크 조각에 사람 번호 매칭
    for i in range(cake_range[0], cake_range[1] + 1):
        if cake_amount[i] == 0:
            cake_amount[i] = idx
# 사람당 케이크 먹는 양 계산
for cake in cake_amount:
    if cake != 0:
        if cake in result:
            result[cake] += 1
        else:
            result[cake] = 1
# 정렬 후 프린트
answer = sorted(result.items(), key=lambda x: x[0])
answer.sort(key=lambda x: x[1], reverse=True)
print(hope_idx)
print(answer[0][0])