# 이진트리순회 (DFS)

# 1. 전위순회 : 부 왼 오
# v : node 값
def DFS(v) :
    if v > 7 :
        # 함수 종료
        return
    else :
        # 함수 본연의 일 (방문) : 먼저 하고 넘어가면 전위순회
        print(v, end= ' ')
        # 왼쪽 자식 노드
        DFS(v*2)
        # 오른쪽 자식 노드
        DFS(v*2+1)

# 2. 중위순회 : 왼 부 오
# v : node 값
def DFS(v) :
    if v > 7 :
        # 함수 종료
        return
    else :
        # 왼쪽 자식 노드
        DFS(v*2)
        # 함수 본연의 일 (방문)
        print(v, end= ' ')
        # 오른쪽 자식 노드
        DFS(v*2+1)

# 3. 후위순회 : 왼 오 부
# v : node 값
def DFS(v) :
    if v > 7 :
        # 함수 종료
        return
    else :
        # 왼쪽 자식 노드
        DFS(v*2)
        # 오른쪽 자식 노드
        DFS(v*2+1)
        # 함수 본연의 일 (방문)
        print(v, end= ' ')

if __name__ = "__main__" :
    DFS(1)