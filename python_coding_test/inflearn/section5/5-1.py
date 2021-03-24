num, m = map(int, input().split())
# str로 만들기 -> 한 글자 씩 빼서 숫자로 만들기
num = list(map(int, str(num)))
stack = []

for x in num :
    # stack : 비어 있지 않으면 True
    while stack and m > 0 and stack[-1] < x :
        # stack의 제일 뒤(=최상단) 요소 빼기
        stack.pop()
        m -= 1
    stack.append(x)

# for문 다 돌아도 m개 만큼 지우지 못한 경우
if m!= 0 :
    # 뒤쪽 m개 날리기
    stack = stack[:-m]
res = ''.join(map(str, stack))
print(res)