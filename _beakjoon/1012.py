import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
n = int(input())

dr = [1,0,-1,0]
dc = [0,1,0,-1]

for asdfasdf in range(n):
    maxc, maxr, bugnum = map(int, input().split())

    bugs = []
    ck = [[0] * maxc for _ in range(maxr)]

    for _ in range(bugnum):
        bc, br = map(int, input().split())
        bugs.append((br,bc))

    cnt = 0

    for i in range(maxr):
        for j in range(maxc):
            if (i,j) in bugs and ck[i][j] == 0 :
                cnt += 1
                Q = deque()
                Q.append((i,j))
                ck[i][j] = 1
                while Q :
                    for _ in range(len(Q)):
                        nr, nc = Q.popleft()
                        for d in range(4):
                            xr = nr + dr[d]
                            xc = nc + dc[d]
                            if xr < 0 or xc < 0 or xr >= maxr or xc >= maxc:
                                continue                        
                            elif (xr,xc) not in bugs:
                                continue
                            elif ck[xr][xc] == 1 :
                                continue
                            else :
                                ck[xr][xc] = 1
                                Q.append((xr,xc))

    print(cnt)
                        

