import sys
sys.stdin = open("/Users/kakao1/Desktop/AA/2-1/input.txt", "rt")

n, m = map(int, input().split())
# index=0은 제외 -> 1부터 시작하게 한다.
cnt = [0] * (n+m+3)
max = -2174000000

for i in range(1, n+1) :
    for j in range(1, m+1) :
        cnt[i+j] += 1

for i in range(n+m+1) :
    if max < cnt[i] :
        max = cnt[i]

for i in range(n+m+1) :
    if cnt[i] == max :
        print(i, end = ' ')