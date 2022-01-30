import sys 

M = 0
X = []
cnt = 0
while True :
    try:
        x = int(sys.stdin.readline())
        X.append(x)
    except:
        break
        
for i in range(len(X)) :
    if X[i] > M :
        M = X[i]
        cnt = i + 1
        
print(M)
print(cnt)