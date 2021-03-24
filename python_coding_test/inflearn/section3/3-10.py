# 스도쿠 검사: 행 탐색, 열 탐색, 그룹 탐색

def check(a) :
    for i in range(9) :
        ch1 = [0]*10 # 행 체크
        ch2 = [0]*10 # 열 체크
        for j in range(9) :
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9 :
            return False
    # 그룹 탐색
    # 1. 그룹 총 9개
    for i in range(3) :
        for j in range(3) :
            # 2. 그룹 내 숫자 9개
            ch3 = [0] * 10
            for k in range(3) :
                for s in range(3) :
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9 :
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a) :
    print("YES")
else :
    print("NO")