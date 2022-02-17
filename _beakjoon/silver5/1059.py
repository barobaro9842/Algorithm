import sys
sys.stdin = open('input.txt', 'r')

# A < B
# A <= x <= B , x not in  S
# 해당 숫자가 어떤 범위에 포함되는지 파악하고, 해당 범위 내에서 만들 수 있는 모든 조합을 구한다.

L = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.append(0)
nums.sort()

A = 0
for i in range(len(nums)-1) :
    if nums[i] == target or nums[i+1] == target:
        A = 0
        break
    elif nums[i] < target and target < nums[i+1]:
        A = (target - nums[i]) * (nums[i+1] - target) - 1
        break

print(A)


