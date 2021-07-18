# str 형식으로 '01'과 같은 것은 eval()으로 문자열 연산 불가능
# -> split 2번 사용해서 숫자 단위로 쪼갠 뒤 int()로 계산
A = input().split('-')
array = []
for i in A:
    sum = 0
    B = i.split('+')
    for j in B:
        if len(j) != 0:
            sum += int(j)
    array.append(sum)
result = array[0]
for i in range(1, len(array)):
    result -= array[i]
print(result)