n = int(input())
a = list(map(int, input().split()))

def reverse(x) :
    res = 0
    while x > 0 :
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x) :
    if x == 1 :
        return False
    # 약수는 절반까지만 봐도 존재하는지 알 수 있으므로 반만 돌면 됨
    for i in range(2, x//2+1) :
        if x % i == 0 :
            return False
    # for 문이 정상적으로 끝났을 때
    else :
        return True
        

for x in a :
    tmp = reverse(x)
    if isPrime(tmp) :
        print(tmp, end = ' ')