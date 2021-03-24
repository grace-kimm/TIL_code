n = int(input())
p = dict()

# 모든 단어 (단어: 1) 쌍으로 딕셔너리에 저장
for i in range(n) :
    word = input()
    p[word] = 1

# 시에 쓰인 단어는 (단어: 0) 쌍으로 변경
for i in range(n-1) :
    word = input()
    p[word] = 0

# p.items() : 딕셔너리 내 key, value 쌍 호출
for key, val in p.items() :
    if val == 1 :
        print(key)