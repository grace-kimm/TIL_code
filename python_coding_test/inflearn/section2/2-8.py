n = int(input())
a = list(map(int, input().split()))

def reverse(x) :
    res = 0
    while x > 0 :
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(X) :
    if x == 1 :
        return False
    # 약수는 절반까지만 존재하므로 반만 돌면 됨
    for i in range(2, x//2+1) :
        if x % i == 0 :
            return False
    else :
        return True
        

for x in a :
    tmp = reverse(x)
    if isPrime(tmp) :
        print(tmp, end = ' ')