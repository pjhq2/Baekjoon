### 백준 3036번 링(S3)
## 최대공약수 셀프 제작
# def gcd(a, b):
#     if max(a,b) % min(a,b) == 0:
#         return min(a,b)
#     else:
#         return gcd(min(a,b), max(a,b)%min(a,b))

# 결국 반지름에 비례함
# 기약분수 전처리 과정
# import math
# N = int(input())
# radius = list(map(int, input().split()))
# for r in radius[1:]:
#     x = math.gcd(radius[0], r)
#     print(f'{int(radius[0]/x)}/{int(r/x)}')