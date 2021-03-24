# 최소 힙
import heapq as hq
a = []

while True :
    n = int(input())
    if n == -1 :
        break
    if n == 0 :
        # heap 비어 있음
        if len(a) == 0 :
            print(-1)
        # heap 있음
        else :
            # a에서 root node를 pop 해준다.
            print(hq.heappop(a))
    else :
        hq.heappush(a, n)