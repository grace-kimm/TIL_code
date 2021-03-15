# 1. 자료형
# 1-1. 정수형
print(round(0.3, 2)) # 소수점 3째자리에서 반올림
# 연산
print(a/b)
print(a//b)
print(a%b)
print(a*b)
print(a**b)

# 1-2. 리스트
a = list()
a = []
a = [0] * n # 크기가 n이고 모든 값이 0인 리스트 초기화
# 인덱싱
print(a[4]) # 다섯번째 원소에 접근
print(a[-1])
print(a[-3])
a[3] = 7 # 4번째 원소 값 변경
print(a[1:4]) # 2번째~4번째 원소까지
# 리스트 컴프리헨션 : 리스트 초기화 방법
array = [i for i in range(20) if i%2 == 1] # 0~19까지 수 중 홀수만 포함하는 리스트
array = [i*i for i in range(1, 10)] # 1~9까지 수의 제곱값을 포함하는 리스트
array = [[0]*m for _ in range(n)] # n*m 크기의 2차원 리스트 초기화
array = [i for i in a if i not in remove_set] # a 리스트에서 remove_set에 없는 원소만 저장
# 리스트 관련 메소드 모음
array.append() # 원소 하나 삽입
array.sort() # 오름차순 정렬
array.sort(reverse=True) # 내림차순 정렬
array.reverse() # 리스트의 원소 순서 모두 뒤집기
array.insert(삽입 위치 인덱스, 삽입 값) # 특정 인덱스 위치에 원소 삽입
array.count('a') # a 원소 개수 세기
array.remove('a') # a 원소 제거 (가장 앞에 있는 1개)

# 1-3. 문자열
a = 'Hello'
b = 'World'
print(a + " " + b) # 문자열 더하기
print(a*3) #문자열 여러번 더하기
print(a[2:4]) # 1번째~3번째 문자열 자르기

# 1-4. 튜플: 그래프 알고리즘(다익스트라 알고리즘 등)에 사용
a = (1, 2, 3, 4) # 값 변경 불가

# 1-5. 딕셔너리
data = dict()
data['사과'] = 'Apple' # 딕셔너리[key] = value
if '사과' in data : # 값 존재 여부 간단히 확인하기
    print('사과 있다')
# 딕셔너리 관련 함수
key_list = data.keys() # key만 담은 함수
value_list = data.values() # value만 담은 함수
for key in key_list : # 각 키에 따른 값을 하나씩 출력
    print(data[key])

# 1-6. 집합: 중복 불가 (특정 데이터 등장 여부 확인할 때 유용)
data = set([1, 1, 2, 3, 4, 4, 5])
data = {1, 1, 2, 3, 4, 4, 5}
# 집합 자료형 연산
print(a | b) # 합집합
print(a % b) # 교집합
print(a - b) # 차집합
# 집합 자료형 관련 함수
data.add(4) # 새로운 원소 추가
data.update([5, 6]) # 새로운 원소 여러 개 추가
data.remove(3) # 특정한 값을 갖는 원소 삭제

# 2. 조건문
if 조건문 1 :
    조건문 1이 true 일 때 실행
elif 조건문 2 :
    조건문 1에 해당하지 않고, 조건문 2가 true 일 때 실행
else :
    위의 모든 조건문이 모두 true가 아닐 때 실행

# 비교 연산자
X == Y # 같다
X != Y # 같지 않다
X > Y # 크다
X < Y # 작다
X >= Y # 크거나 같다
X <= Y # 작거나 같다

# 논리 연산자
X and Y # X와 Y가 모두 참일 때 참(true)
X or Y # X와 Y 중에 하나라도 참이면 참(true)
not X # X가 거짓(false) 일 때 참(true)

# 기타 연산자
X in 리스트 # 리스트 안에 X가 들어가 있을 때 참(true)
X not in 문자열 # 문자열 안에 X가 들어가 있지 않을 때 참(true)

# 조건부 표현식
score = 85
result = 'Success' if score >= 80 else 'Fail'
result = [i for i in a if i no t in remove_set] # 비교) list comprehension

# 3. 반복문
# 3-1. while문
i = 1
result = 0
# i가 9보다 작거나 같고 2의 배수일 때 아래 코드를 반복적으로 실행
while i <= 9 :
    if i % 2 == 0 :
        result += 1
    i+=1

# 3-2. for문: range(시작값, 끝값+1)
scores = [90,85,77,65,97]
cheating_list = [2,4]

for i in range(5) :
    # cheating_list 안에 있으면 해당 학생 무시. 다음번호부터 처리
    if i+1 in cheating_list :
        continue 
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다")

# 구구단 만들기
for i in range(2, 10) :
    for j in range(1, 10) :
        print(i, "x", j, "=", i*j)
    print()

# 4. 함수
def 함수명(매개변수) :
    실행할 소스코드
    return 반환값

# 매개변수 지칭 가능
a = 0
def add(a, b) :
    print(a+b)
add(b=3, a=7)

# 함수 밖의 변수 데이터 변경하기 : global
a = 0
def func():
    global a
    a += 1
for i in range(10) :
    func()
print(a) # a = 10

# 람다 표현식
def add(a, b) :
    print(a+b)
print((lambda a, b: a+b)(a, b))

# 5. 입출력
# 데이터의 개수 입력
n = int(input())
# 데이터를 공백으로 구분해서 int형태 -> 리스트로 입력
data = list(map(int, input().split()))
# 데이터를 공백으로 구분해서 int형태로 입력
n, m, k = map(int, input().split())
# 빠르게 여러 줄의 데이터 입력 받기 (엔터 줄바꿈 제거해서 받기: rstrip())
import sys
data = sys.stdin.readline().rstrip()
print(data)
# 변수 출력
a = 3
b = 7
print(a, b)
# 줄바꿈으로 출력
print(a)
print(b)
# 변수를 문자열로 바꾸어서 출력
print("a는" + str(a) + "입니다.")

# 변수를 콤마(,)로 구분해서 출력
print("a는", a, "입니다.")

# f string 문법으로 출력
print(f"a는 (a)입니다.")