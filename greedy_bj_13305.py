N = int(input()) # 도시의 개수
load_lengths = list(map(int, input().split())) # 도로 길이
oil_prices = list(map(int, input().split())) # 기름 가격

cost = 0
tmp = oil_prices[0]
for idx, oil in enumerate(oil_prices[1:]):
    if oil < tmp: # 더 낮은 가격을 만났을 때
        cost += load_lengths[idx] * tmp
        tmp = oil # tmp에 현재 oil_price 저장
    elif oil >= tmp: # 더 높은 가격 만났을 때
        cost += load_lengths[idx] * tmp
print(cost)