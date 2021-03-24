s = input()
stack = []

for x in s :
    if x.isdecimal() :
        stack.append(int(x))
    else :
        a = stack.pop()
        b = stack.pop()
        if x == '+' :
            stack.append(b + a)
        elif x == '-' :
            stack.append(b - a)
        elif x == '*' :
            stack.append(b * a)
        elif x == '/' :
            stack.append(b / a)
print(stack[0])