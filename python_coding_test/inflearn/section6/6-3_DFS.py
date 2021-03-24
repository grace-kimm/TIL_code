# 부분 집합 구하기 (DFS)
# sol1. DFS 사용 O
def DFS(v) :
    if v == n+1 :
        for i in range(1, n+1) :
            if ch[i] == 1 :
                print(i, end = ' ')
        print()
    else :
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

if __name__ == "__main__" :
    n = int(input())
    ch=[0]*(n+1)
    DFS(1)


# sol2. DFS 사용 X
n = int(input())
n_list = []
for i in range(1, n+1) :
    if (n % i == 0) :
        list.append(i)

for i in range(1, len(n_list) + 1) :
    n_result = combinations(n_list, i)

