n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

# 행, 열 최대값 찾기
for i in range(n) :
    sum1 = sum2 = 0
    for j in range(n) :
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2

# 대각선 최대값 찾기
sum1 = sum2 = 0
for i in range(n) :
    sum1 += a[i][i]
    sum2 += a[i][n-1-i]
if sum1 > largest :
        largest = sum1
if sum2 > largest :
    largest = sum2

print(largest)