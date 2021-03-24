# 총액 동일하게 동전 분배하기 (DFS)

def DFS(L) :
    global res
    if L == n :
        diff = max(money) - min(money)
        if res > diff :
            # 세 사람의 총액 다른지 확인
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3 :
                res = diff
    else :
        for i in range(3) :
            money[i] += coin[L]
            DFS(L+1)
            # back 했을 때
            money[i] -= coin[L]

if __name__ = "__main__" :
    n = int(input())
    coin = []
    for i in range(n) :
        coin.append(int(input()))
    money = [0] * 3
    res = 214000000
    DFS(0)
    print(res)
