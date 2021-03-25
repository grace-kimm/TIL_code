def Count(capacity) :
    cnt = 1 # 필요한 dvd 개수
    sum = 0 # 1장의 dvd 내 누적 된 시간
    for x in Music :
        if sum + x > capacity :
            # x곡 저장 불가 -> 새로운 dvd 필요
            cnt += 1
            sum = x
        else :
            # x곡 저장 가능
            sum += x
    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx = max(Music) # dvd 용량은 한 곡의 용량 보단 커야 함
lt = 1
rt = sum(Music)
res = 0

while lt <= rt :
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m :
        res = mid
        rt = mid - 1 # 더 작은 용량으로도 답이 되는지 찾으러 간다.
    else :
        lt = mid + 1 # 더 큰 용량으로 간다.
print(res)