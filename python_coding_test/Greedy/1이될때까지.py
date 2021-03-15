# Greedy: 1이될때까지 (P99)
# n: 1로 만들 수, k: n을 나눌 수 (n이 k로 나누어 떨어질 때만 사용 가능)

n, k = map(int, input().split())
result = 0

while True :
    # n이 k로 나눠질 때까지 빼기
    target = (n//k) * k
    result += (n - target)
    n = target

    # N이 K보다 작을 때 반복문 탈출
    if n < k :
        break
    # K로 나누기
    result += 1
    n //= k

# n < k 일 때 1이 될때까지 빼기
result += (n-1)
print(result)

