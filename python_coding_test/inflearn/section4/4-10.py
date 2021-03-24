n = int(input())
# 역수열
a = list(map(int, input().split()))
# 원래 수열
ans = []

a = a[::-1]
for x in a :
    ans.insert(x, n)
    n -= 1

for x in ans :
    print(x, end = ' ')