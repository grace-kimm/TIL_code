# 기출 - greedy: 문자열 더하기
# data : 문자열
data = input()
count0 = 0
count1 = 0

# 1번째 원소부터 처리
if data[0] == '1' :
    count0 += 1
else :
    count1 += 1

# 2번째 원소부터 모든 원소를 확인하며
for i in (len(data) - 1) :
    if data[i] != data[i+1] :
        if data[i+1] == '1' :
            count0 += 1
        else :
            count1 += 1

print(min(count0, count1))