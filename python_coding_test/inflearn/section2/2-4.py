import sys
sys.stdin = open("/Users/kakao1/Desktop/AA/2-1/input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a) / len(a), 0)
min = 2147000000

# index, value 모두 출력할 때
for idx, x in enumerate(a) :
    tmp = abs(x-ave) # 평균과 점수의 거리
    if tmp < min :
        min = tmp
        score = x # 거리가 같을 때 비교 위해 점수 저장
        res = idx + 1
    elif tmp == min : # 같은 거리 나오면 큰 점수인 index 선택
        if x > score :
            score = x
            res = idx + 1

print(avg, res)
