# 양팔 저울
def DFS(L, sum) :
    global res
    if L == n :
        if 0 < sum <= s :
            res.add(sum)
    else :
        DFS(L+1, sum+G[L]) # 추 왼쪽에
        DFS(L+1, sum-G[L]) # 추 오른쪽에
        DFS(L+1) # 추 안놓음

if __name__ == "__main__" :
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    # 중복 제거 하면서 가지 수 추가
    res = set()
    DFS(0, 0)
    print(s-len(res))