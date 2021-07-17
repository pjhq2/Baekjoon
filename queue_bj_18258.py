# input() 대신에 sys.stdin.readline() 써서 시간 초과 안뜸
# A = deque()로 해야 시간 초과 안뜸
import sys
from collections import deque
N = int(sys.stdin.readline())
A = deque()
Ans = []
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        A.append(order[1])
    if order[0] == 'pop':
        if len(A) == 0:
            Ans.append(-1)
        else:
            Ans.append(A[0])
            A.popleft()
    if order[0] == 'size':
        Ans.append(len(A))
    if order[0] == 'empty':
        if len(A) == 0:
            Ans.append(1)
        else:
            Ans.append(0)
    if order[0] == 'front':
        if len(A) == 0:
            Ans.append(-1)
        else:
            Ans.append(A[0])
    if order[0] == 'back':
        if len(A) == 0:
            Ans.append(-1)
        else:
            Ans.append(A[-1])
for x in Ans:
    print(x)