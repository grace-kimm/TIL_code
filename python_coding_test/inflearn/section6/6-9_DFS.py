# 수열 추측하기 (DFS)
import sys
def DFS(L, sum) :
    if L == n and sum == f :
        for x in p:
            print(x, end = ' ')
            # 처음 나온 것 보고 프로그램 종료
            sys.exit(0)
    else :
        for i in range(1, n+1) :
            if ch[i] == 0 :
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum+(p[L] * b[L]))
                # back 하면 초기화
                ch[i] = 0


if __name__ = "__main__" :
    n, f = map(int, input().split())
    p = [0] * n # 순열 만들 곳
    b = [1] * n # 이항 계수
    ch = [0] * (n+1) # 중복 피하기
    for i in range(1, n) :
        b[i] = (b[i-1] * (n-i)) // i
    DFS(0, 0)