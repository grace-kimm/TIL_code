# 내 코드
def DFS(L, sum, time) :
    global res
    if time > n :
        return
    if time == n :
        if sum > res :
            res = sum
    else :
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)


if __name__ = "__main__" :
    n = int(input())
    pt = []
    pv = []
    res = -214000000

    for i in range(n) :
        a, b = map(int, input().split())
        pt.append(a)
        pv.append(b)
    
    DFS(0, 0, 0)
    print(res)
    

# 해설
def DFS(L, sum) :
    global res
    if L == n :
        if sum > res :
            res = sum
    else :
        # 내 상담일 + 다음 상담일 <= n+1 이어야 진행 가능
        if L+pt[L] <= n+1 :
            DFS(L+pt[L], sum+pv[L])
        DFS(L+1, sum)


if __name__ = "__main__" :
    n = int(input())
    pt = []
    pv = []
    res = -214000000

    for i in range(n) :
        a, b = map(int, input().split())
        pt.append(a)
        pv.append(b)
    pt.insert(0,0)
    pv.insert(0,0)
    
    DFS(1, 0)
    print(res)
