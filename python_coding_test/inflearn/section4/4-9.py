n = int(input())
a = list(map(int, input().split()))

lt = 0 
rt = n-1
# 새로운 값과 직전에 저장한 값 비교 (직전에 저장한 값 < 새로운 값 이어야 함)
last = 0
# 여기에 결과 누적
res = ""
# 임시 리스트
tmp = []

while lt <= rt :
    if a[lt] > last :
        tmp.append((a[lt], 'L'))
    if a[rt] > last :
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0 :
        break
    else :
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L' :
            lt += 1
        else :
            rt -= 1
    tmp.clear()
print(len(res))
print(res)