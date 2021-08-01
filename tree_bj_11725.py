import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
trees = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

parents = [0 for _ in range(N+1)]
def DFS(node, trees, parents):
    for i in trees[node]:
        if parents[i] == 0:
            parents[i] = node
            DFS(i, trees, parents)

DFS(1, trees, parents)
for i in range(2, N+1):
    print(parents[i])