n = int(input())
body = []
for _ in range(n) :
    a, b = map(int, input().split())
    body.append((a, b))

# a(키) 기준 내림차순 정렬
body.sort(reverse=True)
largest = 0
cnt = 0

for x, y in body :
    if y > largest :
        # 최대값 갱신 -> 선수 될 수 있다.
        largest = y
        cnt += 1
print(cnt)