import sys

# N = int(input())
# X = list(map(int, sys.stdin.readline().split()))

N = 5
X = [20, 10, 35, 30, 7]

m = 1000001
M = -1000001

for i in X :
    if i < m :
        m = i
    if i > M:
        M = i
print(f"{m} {M}")