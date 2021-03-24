from collections import deque
need = input()
n = int(input())

# case 받을 때마다 바로 처리
for i in range(n) :
    plan = input()
    # 새로 읽을 때마다 필수과목 queue 초기화
    dq = deque(need)
    for x in plan :
        # 필수과목인지
        if x in dq :
            if x != dq.popleft() :
                print("#%d NO" % (i+1))
                break
    else :
        if len(dq) == 0 :
            print("#%d YES" % (i+1))
        else :
            print("#%d NO" % (i+1))