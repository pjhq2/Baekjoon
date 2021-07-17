# 동적 프로그래밍을 써야 시간 내에 해결할 수 있다
# 함수 return에 필요한 값들을 튜플로 묶어서 내보냄

d = [0] * 41
cnt0 = [0] * 41
cnt1 = [0] * 41
def fibo(n):
    if n == 0:
        d[0] = 0
        cnt0[0] = 1
        return (d[0], cnt0[0], cnt1[0])
    elif n == 1:
        d[1] = 1
        cnt1[1] = 1
        return (d[1], cnt0[1], cnt1[1])
    else:
        if d[n] != 0:
            return (d[n], cnt0[n], cnt1[n])
        else:
            d[n] = fibo(n-1) + fibo(n-2)
            cnt0[n] = cnt0[n-1] + cnt0[n-2]
            cnt1[n] = cnt1[n-1] + cnt1[n-2]
            return (d[n], cnt0[n], cnt1[n])
T = int(input())
N = []
for i in range(T):
    N.append(int(input()))
for i in N:
    fibo(i)
    print(fibo(i)[1], fibo(i)[2])