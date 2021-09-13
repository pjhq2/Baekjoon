# 1157 단어 공부

chars = input().upper()
word = {}
for char in chars:
    if char in word:
        word[char] += 1
    else:
        word[char] = 1

w = 0
x = ''
flag = False
for k, v in word.items():
    if v == w:
        flag = True
    elif v > w:
        w = v
        x = k
        flag = False

if flag:
    print('?')
else:
    print(x)
