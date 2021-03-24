from collections import deque
n, m = map(int, input().split())
# list에서 pos(번째), value(위험도)를 튜플 형태로 함께 받음
# [(0, 60), (1, 50), (2, 70),,,]
Q = [(pos, val) for pos,val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True :
    cur = Q.popleft()
    # cur[1] = (0, 60)에서 60
    # Q 자료에서 cur[1] 보다 큰 값 있는지 찾는다.
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else :
        cnt += 1
        if cur[0] == m :
            print(cnt)
            break