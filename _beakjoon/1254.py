import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
s = list(input())
orlen = len(s)
cnt = 0

while True :
    print(s)
    if s == s[::-1]:
        break
    s.pop(0)
    cnt += 1

print(orlen + cnt)