# 출발점 -> 도착점 가짓수 (DFS)

# 시계방향
dx = [-1, 0, 1, 0]
dy = [1, 0, -1, 0]

def DFS(x, y) :
    global cnt
    if x == 6 and y == 6 :
        cnt += 1
    else :
        for i in range(4) :
            # 앞으로 갈 방향
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0 :
                board[xx][yy] = 1
                DFS(xx, yy)
                # back 하면 (돌아오면) uncheck
                board[xx][yy] = 0


if __name__ = "__main__" :
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    # 시작 지점 check (back 할때는 uncheck 해줘야 함)
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)