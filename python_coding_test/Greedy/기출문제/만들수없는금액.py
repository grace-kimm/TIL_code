# 기출 - greedy: 만들 수 없는 금액 (어려움)
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data :
    # 만들 수 없는 금액 찾았을 때 반복 종료
    if target < x :
        break
    target += x
print(target)