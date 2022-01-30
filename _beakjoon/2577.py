import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

X = A * B * C

X_str = str(X)

dic = {str(i):0 for i in range(10)}
for i in X_str:
    dic[i] += 1
    
for k, v in dic.items():
    print(v)