import math
x1, y1, r1, x2, y2, r2 = map(int, input().split())
dis = (x2 - x1)**2 + (y2 - y1)**2

if dis == 0 and r1 == r2 :
    print(-1)
elif dis == r1 + r2 or dis == abs(r2-r1) :
    print(1)
elif dis > r1+r2 or dis < abs(r2-r1):
    print(0)
else:
    print(2)