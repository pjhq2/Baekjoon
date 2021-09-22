# 백준 N과 M(1)

N, M = map(int, input().split())
answer = []

def bt(v, result):
    if v == M:
        answer.append(result[:])
        return
    
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            bt(v+1, result)
            result.remove(i)

bt(0, [])
for result in answer:
    print(*result)
