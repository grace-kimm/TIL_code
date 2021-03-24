import sys
sys.stdin = open("/Users/kakao1/Desktop/AA/2-1/input.txt", "rt")

T = int(input())
for t in range(T) :
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))