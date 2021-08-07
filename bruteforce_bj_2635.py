def solution(n):
    if n == 1:
        return [1, 1, 0, 1]
    result = [n]
    answer = []
    for i in range(1, n):
        result.append(i)
        x = 2
        while True:
            temp = result[x-2] - result[x-1]
            if temp >= 0:
                result.append(temp)
                x += 1
            else:
                if len(answer) < len(result):
                    answer = result
                result = [n]
                break
    return answer

n = int(input())
x = solution(n)

print(len(x))
print(' '.join(map(str, x)))