n = int(input())

# solution 1
for i in range(n) :
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2) :
        if s[j] != s[-j-1] :
            print("#%d NO" % (i+1))
            break
    else :
        print("#%d YES" % (i+1))


# solution 2
for i in range(n) :
    s = input()
    s = s.upper()
    if s == s[::-1] :
        print("#%d YES" % (i+1))
    else :
        print("#%d NO" % (i+1))