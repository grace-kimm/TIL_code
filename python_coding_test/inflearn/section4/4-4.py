# distance에 대한 count 세기
def Count(len) :
    cnt = 1
    # 말 배치 start point
    ep = Line[0]
    for i in range(1, n) :
        if (Line[i] - ep) >= len :
            cnt += 1
            ep = Line[i]
    return cnt

n, c = map(int, input().split())
Line = []
for _ in range(n) :
    tmp = int(input())
    Line.append(tmp)
Line.sort()

# 최소거리
lt = 1
# 최대거리
rt = Line[n-1]

# 최대 거리 구하기
while lt <= rt :
    mid = (lt + rt) // 2
    if Count(mid) >= c :
        res = mid
        lt = mid + 1
    else :
        rt = mid - 1
print(res)