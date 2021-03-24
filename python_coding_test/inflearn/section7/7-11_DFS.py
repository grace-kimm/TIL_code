# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y) :
    global cnt
    if x == ex and y == ey :
        cnt += 1
    else :
        for k in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y] :
                # 지나갈거니까 check
                ch[xx][yy] = 1
                DFS(xx, yy)
                # back 했을 때 uncheck
                ch[xx][yy] = 0

if __name__ = "__main__" :
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]

    # 최댓값, 최솟값 필요
    max = -214000000
    min = 214000000

    # board 입력 받기
    for i in range(n) :
        tmp = list(map(int, input().split()))
        for j in range(n) :
            if tmp[j] < min :
                min = tmp[j]
                # 시작 지점
                sx = i
                sy = j
            if tmp[j] > max :
                max = tmp[j]
                # 도착 지점
                ex = i
                ey = j
            # board에 1행씩 입력
            board[i][j] = tmp[j]

    # 가짓수 받을 곳
    cnt = 0

    # 시작 지점 check
    ch[sx][sy] = 1

    DFS(sx, sy)
    print(cnt)
