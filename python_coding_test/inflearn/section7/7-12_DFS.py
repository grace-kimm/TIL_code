# 단지 번호 붙이기 (DFS)

# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y) :
    global cnt

if __name__ = "__main__" :
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                cnt = 0
                DFS(i, j)