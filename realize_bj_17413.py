S = input()
tag = False
result = ''
word = ''
for idx, s in enumerate(S):
    if s == '>':
        result += word + s
        word = ''
        tag = False
    elif s == '<':
        result += word[::-1]
        word = '<'
        tag = True
    elif s == ' ' and tag == False:
        result += word[::-1] + s
        word = ''
    elif idx == len(S) - 1:
        if s == '>':
            result += word + s
        else:
            word += s
            result += word[::-1]
    else:
        word += s
print(result)