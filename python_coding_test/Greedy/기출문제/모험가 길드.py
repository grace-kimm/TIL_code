# 기출 - greedy: 모험가 길드
# n : 모험가의 수
n = int(input())
data = list(map(int, input()))

data.sort()
group = 0 # 총 그룹 수
in_group = 0 # 그룹 내 사람 수

for i in data :
    in_group += 1
    if in_group >= i :
        group += 1 # 그룹 증가
        in_group = 0 # 그룹 초기화 (새 그룹 만들기)
print(group)
