# 잔돈 거슬러 주는 방법 : 동전 바꿔주기

def DFS(L, sum) :
    global cnt
    # cut edge
    if sum > T :
        return
    if L == k :
        if sum == T :
            cnt += 1
    else :
        for i in range(cn[L]+1) :
            DFS(L+1, sum+(cv[L]*i))

if __name__ == "__main__" :
    T = int(input())
    k = int(input())
    cv = list() # 동전 종류
    cn = list() # 종류 별 개수

    for i in range(k) :
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)