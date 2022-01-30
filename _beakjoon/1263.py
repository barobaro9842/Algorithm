import sys
sys.stdin = open('input.txt','r')

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

print(a)
