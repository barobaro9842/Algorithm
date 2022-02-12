import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

def factorial(n):    
    if n <= 1 :
        return 1
    else :
        return n * factorial(n-1)

for _ in range(t):
    n,m = map(int, input().split())
    print(n,m)
    # mCn
    bridge = factorial(m) // (factorial(m-n) * factorial(n))
    print(bridge)





