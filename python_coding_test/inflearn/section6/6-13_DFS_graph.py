# 경로 탐색 (그래프 DFS)

def DFS(v):
    global cnt
    if v == n :
        cnt += 1
        for x in path :
            print(x, end = ' ')
        print()
    else :
        # 상태 트리 구현
        for i in range(1, n+1): 
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                # back 하는 지점
                path.pop()
                ch[i] = 0

if __name__ = "__main__" :
    n, m = map(int, input().split())
    # 0번은 안쓸 것 (g, ch)
    g = [[0]*(n+1) for _ in range(n+1)]
    ch = [0] * (n+1)

    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path = []
    path.append(1)
    # 1번 노드 스스로 check
    ch[1] = 1
    DFS(1)
    
    print(cnt)