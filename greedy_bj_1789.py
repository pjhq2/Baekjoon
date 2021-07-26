# S - cnt 생각
S =int(input())
total = 0
cnt = 0
while total < S - cnt:
    cnt += 1
    total += cnt
print(cnt)