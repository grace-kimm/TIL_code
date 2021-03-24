# 중복 순열 구하기

def DFS(L) :
    global cnt
    if L == m :
        for j in range(m) :
            print(res[j], end= ' ')
            print()
            cnt = cnt + 1
    else :
        for i in range(1, n+1) :
            res[L] = i # 내 함수가 해야 할 일
            DFS(L+1) # 자식 노드 호출

if __name__ = "__main__" :
    n, m = map(int, input().split())
    # 부분 집합 포함이면 1, 아니면 0으로 표시할 리스트
    res = [0] * n
    # 부분 집합 경우의 수
    cnt = 0
    DFS(0)
    print(cnt)