# 무식하게 구현...

import sys
sys.stdin = open('input.txt')

N = int(input())
store_name = input()
signboards = [input() for _ in range(N)]

cnt = 0
for signboard in signboards:
    start = 0
    gap = 1
    check = False
    while start+(len(store_name)-1)*gap < len(signboard):

        for i in range(len(store_name)):
            if store_name[i] == signboard[start+i*gap]:
                continue
            else:
                start += 1
                if not start+(len(store_name)-1)*gap < len(signboard):
                    start = 0
                    gap += 1
                break

        else:
            check = True
            break

    if check == True:
        cnt += 1

print(cnt)
