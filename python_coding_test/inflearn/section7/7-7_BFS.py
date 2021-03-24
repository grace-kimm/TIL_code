# 송아지 찾기 (BFS)
from collections import deque

# 직선의 좌표 점은 1부터 10000까지
MAX = 10000
# 1부터 시작이므로 MAX +1 로 만들어놓기
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
n, m = map(int, input().split())

# 중복 방문 방지
ch[n] = 1
# 시작점은 점프 횟수 0으로 할당
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ :
    # 현재 지점
    now = dQ.popleft()

    # 도착 지점
    if now == m :
        break

    # 도착 지점 갈 때까지 for문 반복
    for next in (now-1, now+1, now+5) :
        if 0 < next <= MAX :
            if ch[next] == 0 :
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])