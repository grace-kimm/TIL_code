def DFS(L, sum) :
    global res
    # cut edge : res보다 큰 level은 보지 않음
    if L > res :
        return
    # sum > m은 볼 필요 없음
    if sum > m :
        return
    # 최소 level 찾기
    if sum == m :
        if L < res :
            res = L
    else :
        for i in range(n) :
            DFS(L+1, sum+a[i])

if __name__ = "__main__" :
    n = int(input())
    a = map(int, input().split())
    m = int(input())
    # res : 동전 최소 개수
    res = 2147000000
    # 가장 큰 동전부터 계산하기 위해 내림차순 정렬
    a.sort(reverse=True)
    DFS(0, 0)

    print(res)