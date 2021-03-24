n = int(input())
# index=0은 제외 -> 1부터 시작하게 한다.
ch = [0] * (n+1)
# cnt : 소수의 개수
cnt = 0

for i in range(2, n+1) :
    if ch[i] == 0 :
        cnt += 1
        for j in range(i, n+1, i) :
            ch[j] = 1

print(cnt)