from collection import deque
# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# board 입력 받기
board = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * 7 for _ in range(7)]

# Q 만들기
Q = deque()
# 출발 위치에서 시작
Q.append((0, 0))
# 1번 방문하면 다시 방문 X -> 벽으로 check
board[0][0] = 1

# Q가 비어 있으면 멈춘다.
while Q :
    # 시작 위치 pop
    tmp = Q.popleft()
    # 상하좌우
    for i in range(4) :
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0 :
            # 지나갔다 표시
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))
    
    if dis[6][6] == 0 :
        print(-1)
    else :
        print(dis[6][6])