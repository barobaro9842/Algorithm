import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt','r')
n, target = map(int,input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

total = 0
res = 0

for coin in coins :
    cnt = 1
    while total + coin * cnt < target :
        cnt += 1
        total = total + coin * cnt
    res += cnt

print(total)