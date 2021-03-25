# 랜선 자르기 (결정 알고리즘)

# 각 랜선에서 나올 수 있는 짧은 랜선의 수
def Count(len) :
    cnt = 0
    for x in Line : # k개
        cnt += (x // len)
    return cnt

k, n = map(int, input().split())
Line = []
res = 0
largest = 0

for i in range(k) :
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt :
    mid = (lt+rt) // 2 # 랜선 길이
    if Count(mid) >= n :
        res = mid
        lt = mid + 1 # 더 긴 것도 가능한지 check
    else :
        rt = mid - 1 # 더 짧은 걸로 확인
print(res)
