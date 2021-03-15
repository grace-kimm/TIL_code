# greedy: 큰 수의 법칙 (p92)
# 배열의 크기 n, 숫자가 더해지는 횟수 m, 한번에 중복 가능 횟수 k

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort()
first = data[-1]
second = data[-2]

# first가 더해질 수
count = int(m / (k+1)) * k
count += m - (m % (k+1))

result = count * first + (m-count) * second