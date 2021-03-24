# 사과나무 (BFS)

import collections import deque
# 시계방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 중복 방지 check list
ch = [[0]*n for _ in range(n)]
# 사과 총 개수
sum = 0
Q = deque()

# 출발점 (격자의 중심)
ch[n//2][n//2] = 1
sum += a[n//2][n//2]
Q.append((n//2, n//2))
L = 0

while True: 
    # 다 돌았을 때 (중심에서 2번 가면 한 쪽의 끝까지 가는 것)
    if L == n//2 :
        break
    
    size = len(Q)
    # for i 돌리면 각 level 탐색
    for i in range(size) :
        tmp = Q.popleft()
        for j in range(4) :
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0 :
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1

print(sum)