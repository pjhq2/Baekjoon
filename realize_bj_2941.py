word = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = len(word)
for c in cro:
    result -= word.count(c)
print(result)