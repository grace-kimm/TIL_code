n, m = map(int, input().split())
a = list(map(int, input().split()))

# 리스트 내 lt, rt가 있음 -> lt 부터 rt 미만까지 -> loop 돌면서 적절한 값 찾는다.
# tot>m : rt + 1 / tot=m : cnt+1 & tot=0 / tot<m : lt + 1
# lt = rt : tot=0
# lt > rt : 불가
# lt = rt = n이면 종료

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True :
    if tot < m :
        if rt < n :
            tot += a[rt]
            rt += 1
        else :
            break
    elif tot == m :
        cnt += 1
        tot -=a[lt]
        lt+=1
    else :
        tot -= a[lt]
        lt+=1
print(cnt)
