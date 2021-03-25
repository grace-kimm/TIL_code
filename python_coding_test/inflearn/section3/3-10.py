# 스도쿠 검사: 행 탐색, 열 탐색, 그룹 탐색

def check(a) :
    # 가로 세로 탐색
    for i in range(9) : # 행
        ch1 = [0]*10 # 행 체크
        ch2 = [0]*10 # 열 체크
        for j in range(9) : # 행, 열
            ch1[a[i][j]] = 1 # 0행 체크
            ch2[a[j][i]] = 1 # 0열 체크
        if sum(ch1) != 9 or sum(ch2) != 9 :
            return False

    # 그룹 탐색
    # 1. 그룹 총 9개
    # i, j : 9개 그룹
    for i in range(3) :
        for j in range(3) :
            # 2. 그룹 내 숫자 9개
            # k, s : 9개 숫자
            # 그룹 1개 할 때마다 check list 초기화
            ch3 = [0] * 10
            for k in range(3) :
                for s in range(3) :
                    # i*3+k : 행, j*3+s : 열
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9 :
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
# check 함수가 true 일 때만 YES
if check(a) :
    print("YES")
else :
    print("NO")