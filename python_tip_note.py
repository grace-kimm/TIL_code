# 파이썬 알고리즘 tips

# 1. 최소값 구하기
arr = [5, 3, 7, 8, 2, 5, 2, 6]
arrMin = float('inf')
for i in range(len(arr)) :
    if arr[i] < arrMin :
        arrMin = arr[i]

# 2. 소수의 개수 세기 (에라토스테네스 체)
n = int(input())
# index=0은 제외 -> 1부터 시작하게 한다.
ch = [0] * (n+1)
# cnt : 소수의 개수
cnt = 0
for i in range(2, n+1) :
    if ch[i] == 0 :
        cnt += 1
        for j in range(i, n+1, i) : # i의 배수들은 모두 1로
            ch[j] = 1
print(cnt)

# 2-1. 특정 숫자가 소수인지 판별하기
def is_prime_number(x) :
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return False # 소수 아님
    return True # 소수
print(is_prime_number(4))
print(is_prime_number(7))

# 3. n번 input이 들어오고 이걸 행렬 테이블로 만들 때
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 4. 상하좌우 모두 확인할 때
# dx, dy 리스트 선언
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# all, any 함수 -> true, false 반환
cnt = 0
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)) :
            cnt += 1
print(cnt)

# 5. 투 포인터 : 부분합의 수 구하기(start, end), 정렬 된 리스트의 합집합 구하기(a, b pointer), 구간 합 구하기(prefix)

# 5-1. 부분합의 수 구하기
# 1) 현재 부분 합 == M : cnt + 1
# 2) 현재 부분 합 < M : end + 1 (부분 합 증가)
# 3) 현재 부분 합 > M : start + 1 (부분 합 감소)
# 조건: end < n
n = 5 # 데이터 수
m = 5 # 찾고자 하는 합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n) :
    while interval_sum < m and end < n :
        interval_sum += data[end]
        end += 1
    if interval_sum == m :
        count += 1
    # 위 2개 조건을 만족하지 않고 위 문장 다 시행하면
    interval_sum -= data[start]
print(count)

# 5-2. 정렬 된 리스트의 합집합 구하기
n, m = 3, 4 # n: a리스트 수, m: b리스트 수
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n+m)
i = 0 # a pointer
j = 0 # b pointer
k = 0 # result pointer

while i < n or j < m :
    # 리스트 b의 원소가 모두 처리 되었거나, a의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]) :
        # 리스트 a의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i += 1
    # 리스트 a의 원소가 모두 처리 되었거나, b의 원소가 더 작을 때
    else :
        result[k] = b[j]
        j += 1
    k += 1
# 결과 리스트 출력
for i in result :
    print(i, end = ' ')

# 5-3. 구간합 구하기: prefix
# 데이터의 개수 n
n = 5
data = [10, 20, 30, 40, 50]

# prefix 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data :
    sum_value += i
    prefix_sum.append(sum_value)
# 구간 합 계산 (3번째 ~ 4번째 수)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])


# 6-1. 다익스트라 알고리즘: 우선순위 큐, 최단거리
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한값

# 노드 개수, 간선 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드에 연결 되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
# 모든 간선 정보 입력 받기
for _ in range(m) :
    a, b, c = map(int, input().split())
    # a -> b 비용이 c
    graph[a].append((b, c))

def dijkstra(start) :
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해(자기 자신) q에 삽입 : (거리, 이동할 곳 노드)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q : # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 실행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1) :
    # 도달할 수 없는 경우 INFINITY 출력
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])
