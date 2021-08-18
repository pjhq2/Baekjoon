# 이거 어렵게 생각하면 어려운데 쉽게 생각하면 쉽고
# 처음에 방향을 잘못 잡으면 어렵게 풀게된다.
for tc in range(4):

    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 공통부분이 없음
    if x1 > p2 or x2 > p1 or y1 > q2 or y2 > q1:
        print('d')
    # 점
    elif (x1 == p2 or x2 == p1) and (y1 == q2 or y2 == q1):
        print('c')
    # 선분
    elif x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
        print('b')
    # 직사각형
    else:
        print('a')