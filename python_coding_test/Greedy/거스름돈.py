# Greedy: 거스름돈 (p87)
# 거스름돈끼리 배수 관계여야 사용 가능
n = 1260
count = 0

# 큰 단위 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types :
    count += n // coin_types
    n = n % coin_types
print(count)