board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# 0, 1, 2 열에서 출발해야 5개 숫자 잡을 수 있음
for i in range(3):
    # 7개 행
    for j in range(7):
        # 행 내 비교
        tmp = board[j][i:i+5] # 5개 숫자 자르기
        if tmp == tmp[::-1] :
            cnt += 1
        # 열 내 비교
        for k in range(2) :
            if board[i+k][j] != board[i+5-k-1][j] :
                break
        else :
            cnt += 1
print(cnt)