# N을 입력받기
n = int(input())
x, y = 1, 1     # 초기점
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_steps = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans :
    # 이동 후 좌표 구하기(nx)
    for i in range(len(move_steps)) :
        if plan == move_steps[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시
    if nx < 1 or nx > n or ny < 1 or ny > n :
        continue
    # nx로 이동 수행
    x, y = nx, ny

print(x, y)