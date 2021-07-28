import math

N = input()
number_list = [0 for _ in range(10)]
for n in N:
    number_list[int(n)] += 1
number_list[6] += number_list[9]
number_list[6] = math.ceil(number_list[6]/2)
print(max(number_list[:-1]))