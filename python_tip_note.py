# 파이썬 알고리즘 tips

# 1. 최소값 구하기
arr = [5, 3, 7, 8, 2, 5, 2, 6]
arrMin = float('inf')
for i in range(len(arr)) :
    if arr[i] < arrMin :
        arrMin = arr[i]

# 2. 소수 (에라토스테네스 체)
n = int(input())
# index=0은 제외 -> 1부터 시작하게 한다.
ch = [0] * (n+1)
# cnt : 소수의 개수
cnt = 0

for i in range(2, n+1) :
    if ch[i] == 0 :
        cnt += 1
        for j in range(i, n+1, i) : # i의 배수들은 모두 1로
            ch[j] = 1
print(cnt)

# 3. n번 input이 들어오고 이걸 행렬 테이블로 만들 때
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 4. 상하좌우 모두 확인할 때
# dx, dy 리스트 선언
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# all, any 함수 -> true, false 반환
cnt = 0
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)) :
            cnt += 1
print(cnt)

