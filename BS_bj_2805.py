import sys

N, M = list(map(int, input().split()))
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

def cut_tree(start, end, trees):
    while start <= end:
        total = 0
        cut = (start + end) // 2
        for tree in trees:
            if tree > cut:
                total += (tree - cut)
        if total < M:
            end = cut - 1
        else:
            result = cut
            start = cut + 1
    return result

print(cut_tree(0, trees[-1], trees))