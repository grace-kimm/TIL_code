# 기출 - greedy: 곱하기 혹은 더하기
# s : 문자열
s = input()
# 1번째 글자 넣고 시작
result = int(s[0])

for i in s :
    num = int(i)
    if result <= 1 or num <= 1 :
        result += num
    else :
        result *= num

print(result)