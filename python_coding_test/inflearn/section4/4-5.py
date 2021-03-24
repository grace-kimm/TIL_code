n = int(input().split())
meeting = []
for _ in range(n) :
    s, e = map(int, input().split())
    # s, e를 tuple 자료형으로 포함
    meeting.append((s, e))
# 끝나는 시간 기준 정렬 : 기준은 x[1]이 우선, x[0]이 다음
meeting.sort(key=lambda x : (x[1], x[0]))

# 현재 회의의 end time
et = 0
cnt = 0
for s, e in meeting :
    if s >= et :
        et = e
        cnt += 1
print(cnt)
