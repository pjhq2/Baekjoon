N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort()
result = []
for i in range(N):
    result.append(rope[i] * (N-i))
print(max(result))