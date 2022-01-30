import sys

# N = int(input())
# X = list(map(int, sys.stdin.readline().split()))
X = [40, 80, 60]
M = max(X)
for i in range(len(X)):
    X[i] = X[i]/M * 100

print(sum(X)/len(X))