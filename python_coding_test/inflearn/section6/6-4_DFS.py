# 합이 같은 부분집합 (DFS)
import sys
def DFS(L, sum) :
    if sum > total // 2 :
        return
    # 다 돌았다.
    if L == n :
        if sum == (total - sum) :
            print("YES")
            # 프로그램 전체 종료 - 0 : 정상 종료 / 1 : 비정상 종료
            sys.exit(0)
    else :
        # 이번 원소를 더한다.
        DFS(L+1, sum+a[L])
        # 이번 원소를 안더한다.
        DFS(L+1, sum)


if __name__ = "__main__" :
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")