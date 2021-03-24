n = int(input())
boxes = list(map(int, input().split()))
m = int(input())
boxes.sort()

for _ in range(m) :
    boxes[0] += 1
    boxes[n-1] -= 1
    boxes.sort()
print(boxes[n-1] - boxes[0])