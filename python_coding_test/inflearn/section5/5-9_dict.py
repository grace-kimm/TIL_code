# 1번째 방법
a = input()
b = input()
a_dict = {}
b_dict = {}

for i in a :
    a_dict[i] = a_dict.get(i, 0) + 1

for j in b :
    b_dict[j] = b_dict.get(j, 0) + 1

# 같은지 확인방법 1
if a_dict == b_dict :
    print("YES")
else :
    print("NO")

# 같은지 확인방법 2
for i in a_dict.keys() :
    if j in b_dict.keys() :
        if a_dict[i] != b_dict[j] :
            print("NO")
            break
    else :
        print("NO")
        break
else :
    print("YES")


# 2번째 방법
a = input()
b = input()
sH = dict()
for x in a :
    sH[x] = sH.get(x, 0) + 1
for x in a :
    sH[x] = sH.get(x, 0) - 1
for x in a :
    if sH.get(x) > 0 :
        print("NO")
        break
else :
    print("YES")