def Count(capacity) :
    # 필요한 dvd 개수
    cnt = 1
    # 1장의 dvd 내 누적 된 시간
    sum = 0
    for x in Music :
        if sum + x > capacity :
            cnt += 1
            sum = x
        else :
            sum += x
    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx = max(Music)
lt = 1
rt = sum(Music)
res = 0

while lt <= rt :
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m :
        res = mid
        rt = mid - 1
    else :
        lt = mid + 1
print(res)