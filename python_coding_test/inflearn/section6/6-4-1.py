# 전역변수와 지역변수

# 1. 리스트 일 때
def DFS() :
    global a
    a = a + [4]
    print(a)

if __name__ == "__main__" :
    a = [1, 2, 3]
    DFS()
    print(a)

# 2. int 일 때
def DFS() :
    global a
    a = a + 4
    print(a)

if __name__ == "__main__" :
    a = 3
    DFS()
    print(a)