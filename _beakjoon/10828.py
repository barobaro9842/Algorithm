import sys
sys.stdin = open('input.txt', 'r')
n = int(input())

stack = []
for _ in range(n) :
    cmd = sys.stdin.readline().rstrip()
    if cmd[:4] == 'push':
        cmd = cmd.split()
        if cmd[0] == 'push' :
            stack.append(int(cmd[1]))
    else :
        if cmd == 'top' :
            print(stack[-1] if stack else -1)
        if cmd == 'size' :
            print(len(stack))
        if cmd == 'empty' :
            print(0 if stack else 1)
        if cmd == 'pop' :
            print(stack.pop() if stack else -1)