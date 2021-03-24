def DFS(L, sum, tsum) :
    global result
    # cut edge 1. 현재 강아지 무게 + 남은 강아지 다 더했을 때 무게 < 현재 max 이면 계산 안한다.
    if sum + (total - tsum) < result :
        return
    # cut edge 2. 현재 강아지 무게 > 최대 실을 수 있는 무게(c) 이면 계산 안한다.
    if sum > c :
        return
    
    # 강아지 다 돌았으니 멈춘다.
    if L == n :
        if sum > result :
            result = sum
    else :
        # tsum : 판단을 한 강아지들의 무게
        DFS(L+1, sum+a[L], tsum + a[L])
        DFS(L+1, sum, tsum + a[L])

if __name__ == "__main__" :
    c, n = map(int, input().split())
    a = [0] * n
    result = -2147000000

    for i in range(n) :
        a[i] = int(input())
    total = sum(a)
    
    DFS(0, 0, 0)
    print(result)