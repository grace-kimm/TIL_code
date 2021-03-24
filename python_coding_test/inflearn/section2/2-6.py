n = int(input())
a = list(map(input().split()))

# 1번째 방법
def digit_sum(x) :
    sum = 0
    while x > 0 :
        sum += x % 10
        x = x // 10
    return sum

# 2번째 방법
def digit_sum(x) :
    sum = 0
    for i in str(x) :
        sum += int(i)

max = -2147000000
for x in a :
    tot = digit_sum(x)
    if tot > max :
        max = tot
        res = x
print(rex)