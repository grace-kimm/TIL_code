# 공주 구하기
from collections import deque
n, k = map(int, input().split())
# queue 만들기 : 1 ~ n까지
dq = list(range(1, n+1))
dq = deque(dq)

# queue가 빌 때 멈춘다.
while dq :
    # k-1번째까지는 popleft & append
    for _ in range(k-1) :
        cur = dq.popleft()
        dq.append(cur)
    # k번째는 popleft only
    dq.popleft()
    # 1명 남으면 완료
    if len(dq) == 1 :
        print(dq[0])
        dq.popleft()
