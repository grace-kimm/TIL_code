# 파이썬 표준 라이브러리

# 1. 내장 함수: sum, min, max, eval, sorted, sort
# 1-1. sum
result = sum([1, 2, 3, 4, 5])
# 1-2. min
result = min([1, 2, 3, 4, 5])
# 1-3. max
result = max([1, 2, 3, 4, 5])
# 1-4. eval : 수학 수식이 문자열로 들어오면 해당 수식을 계산한 결과 반환
result = eval("(3+5)*7") # 56
# 1-5. sorted : iterable 객체의 정렬 결과 반환. 기준(key), 정렬(reverse) 설정 가능
result = sorted([9, 1, 8, 5, 4]) # 오름차순 정렬
result = sorted([9, 1, 8, 5, 4], reverse=True) # 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75)], key = lambda x: x[1]) # 2번째 요소 기준 정렬
# 1-6. sort : 리스트 객체의 내부 값이 정렬된 값으로 바로 변경됨
data = [9, 1, 8, 5, 4]
data.sort() # [1, 4, 5, 8, 9]

# 2. itertools : permutations, combinations
# 2-1. permutations: 모든 순열 구하기. 순서 바뀐 것은 별도로 생각
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 3개 뽑는 순열
result = list(permutations(data)) # 모든 순열

# 2-2. combinations : 모든 조합 구하기. 순서 바뀐 것은 같은 것으로 생각
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 3)) # 3개 뽑는 조합
result = list(combinations(data)) # 모든 조합

# 2-3. product : r개의 데이터를 뽑아 나열하는 모든 경우(순열), 단 중복(A, A) 허용
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개 뽑는 모든 순열 구하기(중복 허용)

# 2-4. combination_with_replacement: 모든 조합 구하기, 단 중복(A, A) 허용
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2)) # 2개 뽑는 모든 조합 구하기(중복 허용)

# 3. heapq : 힙 제공(최소힙). 우선순위 큐 기능 구현에 사용
import heapq
# 힙 정렬 구현 (오름차순)
def heapsort(iterable) :
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 : heappush
    for value in iterable :
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 : heappop
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result
result = heapsort([1, 3, 5, 7, 9, 0])
print(result) # [0, 1, 3, 5, 7, 9]

# 최대 힙 & 힙 정렬 (내림차순) 구현
def heapsort(iterable) :
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 : 부호 반대로 바꾸어 넣음
    for value in iterable :
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 : 부호 다시 반대로 해줌
    for i in range(len(h)) :
        result.append(-heapq.heappop(h))
    return result
result = heapsort([1, 3, 5, 7, 9, 0])
print(result) # [9, 7, 5, 3, 1, 0]

# 4. bisect : 이진 탐색. '정렬된 배열'에서 특정한 원소 찾을 때 효과적
# bisect_left(a, x) : 정렬 된 순서를 유지하면서 리스트 a에 데이터 x(값)를 삽입할 가장 왼쪽 인덱스 찾기
# bisect_right(a, x) : 정렬 된 순서를 유지하면서 리스트 a에 리스트 x(값)를 삽입할 가장 오른쪽 인덱스 찾기
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x)) # 2 (3번째)
print(bisect_right(a, x)) # 4 (5번째)

# '정렬된 리스트'에서 '값이 특정 범위에 속하는 원수의 개수' 구하기
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수 반환하는 함수
# -1에서 시작하면 RV 포함. 0에서 시작하면 RV 미포함
def count_by_range(a, left_value, right_value) :
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
a = [1, 2, 3, 3, 3, 3, 4, 4, 8  9]
print(count_by_range(a, 4, 4)) # 값이 4인 개수 : 2
print(count_by_range(a, -1, 3)) # 값이 -1 ~ 3 사이 : 6

# 5. collections : deque, Counter
# 5-1. deque : 큐를 구현 - popleft(), append()
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1) # 가장 왼쪽에 1 삽입
data.append(5) # 가장 오른쪽에 5 삽입
data.popleft() # 가장 왼쪽 요소 빼기
data.pop() # 가장 오른쪽 요소 빼기
print(data) # [2, 3, 4]

# 5-2. Counter : 등장 횟수 세기. 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # 3
print(counter['green']) # 1
print(dict(counter)) # {'red':2, 'blue':3, 'green':1}

# 6. math: factorial, sqrt, gcd, pi, e
import math
print(math.factorial(5)) # 120
print(math.sqrt(9)) # 3 (제곱근)
print(math.gcd(21, 14)) # 최대공약수
# 최소공배수를 구하는 함수
def lcm(a, b) :
	return a * b // math.gcd(a, b)
print(lcm(21, 14)) # 최소공배수
print(math.pi) # pi 출력
print(math.e) # 자연상수 e 출력
