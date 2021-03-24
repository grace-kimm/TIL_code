a = input()
b = input()
# 대문자 26개, 소문자 26개
str1 = [0] * 52
str2 = [0] * 52

for x in a :
    if x.isupper() :
        # A의 ASCII num = 65 -> 0부터 시작하게 만들어주기
        str1[ord(x)-65] += 1
    else :
        # a의 ASCII num = 97 -> 26부터 시작하게 만들어주기
        str1[ord(x)-71] += 1

for x in b :
    if x.isupper() :
        # A의 ASCII num = 65 -> 0부터 시작하게 만들어주기
        str2[ord(x)-65] += 1
    else :
        # a의 ASCII num = 97 -> 26부터 시작하게 만들어주기
        str2[ord(x)-71] += 1

for i in range(52) :
    if str1[i] != str2[i] :
        print("NO")
        break
else :
    print("YES")