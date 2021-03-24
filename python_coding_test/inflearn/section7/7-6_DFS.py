# 암호화 복호화 (DFS)
def DFS(L, P) :
    if L == n :
        cnt += 1
        for j in range(P) :
            print(res[j], end='')
        print()
    else :
        for i in range(1, 27) :
            # 한자리 수가 같을 때
            if code[L] == i :
                res[P] = i
                DFS(L+1, P+1)
            # 두자리 수가 같을 때
            elif i>=10 and code[L] == (i//10) and code[L+1] == (i%10) :
                res[P] = i
                DFS(L+2, P+1)

if __name__ = "__main__" :
    code = list(map(int, input().split()))
    n = len(code)
    # 2자리 씩 비교할 때 index out of range 방지하기 위해 맨 뒤에 1칸 추가
    code.insert(n, -1)
    # 가능한 답 출력
    res = [0] * (n+3)
    # 경우의 수 cnt
    cnt = 0
    DFS(0, 0)