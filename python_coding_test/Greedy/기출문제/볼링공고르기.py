# 기출 - greedy: 볼링공 고르기

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data :
    # 각 무게에 해당하는 볼링공 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리 (A 기준)
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) n에서 제외 - A가 선택하면 B는 같은 것 선택 불가
    result += array[i] * n  # A가 i를 선택하는 경우의 수 * B가 i 외에 다른 것을 선택하는 경우의 수 (B의 선택은 i보다 커야 함)