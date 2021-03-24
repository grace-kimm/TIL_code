a = input()
res = ''
stack = []

for x in a :
    if x.isdecimal() :
        res += x
    else :
        # 여는 괄호는 스택에 쌓기
        if x == '(' :
            stack.append(x)
        elif x == '*' or x == '/' :
            # 스택에 쌓인 연산자가 *, / 이면 쌓인 애부터 처리
            while stack and (stack[-1]=='*' or stack[-1]=='/') :
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-' :
            # 여는 괄호는 닫는 괄호 만나기 전까지는 스택 안에 있음
            # 그 외 쌓인 연산자는 처리
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.append(x)
        elif x == ')' :
            # 여는 괄호 외 다른 연산자는 모두 처리
            while stack and (stack[-1] != '('):
                res += stack.pop()
            # 여는 괄호는 그냥 빼주기 : 괄호는 res에 포함 안됨
            stack.pop()

# 스택에 남은 애들 다 처리
while stack :
    res += stack.pop()
