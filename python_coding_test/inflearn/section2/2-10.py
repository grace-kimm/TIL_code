n = int(input().split())
a = list(map(int, input().split()))
sum = 0
# 가중치
cnt = 0

for x in a :
    if x == 1 :
        cnt += 1
        sum += cnt
    else :
        cnt = 0
print(sum)