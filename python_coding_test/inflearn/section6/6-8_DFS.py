# 순열 구하기 (DFS)

def DFS(L) :
    global cnt
    if L == m :
        for j in range(m) :
            print(res[j], end = ' ')
        print()
        cnt += 1
        print(cnt)
    else :
        for i in range(1, n+1) :
            if ch[i] == 0 :
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                # 다 처리하고 back 해서 다음 경우의 수로 가니까 초기화 필요
                ch[i] = 0
            res[L] = i
            DFS(L+1)


if __name__ = "__main__" :
    n, m = map(int, input().split())
    # L 관련
    res = [0] * n
    # n 관련
    ch = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)