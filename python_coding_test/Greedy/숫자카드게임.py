# Greedy: 숫자카드게임 (P96)
# n: 행 개수, m: 열 개수
n, m = map(int, input().split())
result = 0

for i in range(n) :
    data = list(map(int, input().split()))
    data.sort()

    min_data = min(data)
    result = max(result, min_data)