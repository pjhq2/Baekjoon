import sys

M = int(input())
S = set()
result = []
for _ in range(M):
    arith = sys.stdin.readline().split()
    if arith[0] == 'add':
        if int(arith[1]) not in S:
            S.add(int(arith[1]))
    elif arith[0] == 'remove':
        if int(arith[1]) in S:
            S.remove(int(arith[1]))
    elif arith[0] == 'check':
        if int(arith[1]) in S:
            print(1)
        else:
            print(0)
    elif arith[0] == 'toggle':
        if int(arith[1]) in S:
            S.discard(int(arith[1]))
        else:
            S.add(int(arith[1]))
    elif arith[0] == 'all':
        S = set(range(1, 21))
    elif arith[0] == 'empty':
        S.clear()