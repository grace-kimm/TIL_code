a, b = map(int, input().split())
# swap
a, b = b, a

# 0~20 list
a = list(range(21))
# _ : 변수 없이 그냥 반복
for _ in range(10) :
    s, e = map(int, input().split())
    # 바꾸는 수 : (e-s+1) // 2
    for i in range((e-s+1)//2) :
        a[s+i], a[e-i] = a[e-i], a[s+i]
# 0 제거
a.pop(0)
for x in a:
    print(x, end=' ')