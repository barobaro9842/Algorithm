import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

nums = list(map(int, input().split()))
A = max(nums) * min(nums)
print(A)