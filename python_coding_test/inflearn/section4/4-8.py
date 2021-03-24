# sol1. List 자료구조
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

# 구명보트 수
cnt = 0

# p가 비어있지 않은 동안 실행
while p :
    if len(p) == 1 :
        cnt += 1
        break
    if p[0] + p[-1] > limit :
        p.pop()
        cnt += 1
    else :
        p.pop(0)
        p.pop()
        cnt += 1

print(cnt)



# sol2. deque 자료구조
from collections import deque
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)
# 구명보트 수
cnt = 0
# p가 비어있지 않은 동안 실행
while p :
    if len(p) == 1 :
        cnt += 1
        break
    if p[0] + p[-1] > limit :
        p.pop()
        cnt += 1
    else :
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)