import sys
sys.stdin = open("/Users/kakao1/Desktop/AA/2-1/input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a) / len(a), 0)
min = 2147000000

for idx, x in enumerate(a) :
    tmp = abs(x-ave)
    if tmp < min :
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min :
        if x > score :
            score = x
            res = idx + 1

print(ave, res)
