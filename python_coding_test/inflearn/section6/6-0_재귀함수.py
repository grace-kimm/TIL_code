# 재귀함수와 스택
# 재귀함수 : 반복문의 대체재

def DFS(x) : 
    if x > 0 :
        DFS(x-1)
        print(x, end= ' ')
# print(x) 다음 DFS(x-1) 실행 : 3 2 1
# DFS(x-1) 다음 print(x) 실행 : 1 2 3

# main 함수와 재귀함수 구분 : 여기부터 실행 됨
if __name__ == "__main__" :
    n = int(input())
    DFS(n) 