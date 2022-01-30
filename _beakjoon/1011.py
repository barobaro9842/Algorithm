import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
case = int(input())

for cascascasc in range(case):
    s, e = map(int, input().split())

    Q = deque()     # 현재 위치
    ck = [0] * (e-s) # 방문 체크
    dis = [0] * (e-s) # 거리 업데이트

    Q.append((0,0)) # 시작점 # 이동중심점
    ck[0] = 1  #시작점 방문체크

    while Q :
        for _ in range(len(Q)) :
            p, m = Q.popleft() # 시작점, 0
            for i in [-1,0,1] :
                np = p + m + i #다음 이동 지점
                nm = m + i # 다음 이동범위의 중점
                if nm <= 0 or np > e-1-s : #범위를 초과한 경우
                    continue
                else :
                    if ck[np] == 0: #노방문
                        ck[np] = 1
                        dis[np] = dis[p] + 1
                        Q.append((np, nm))
    print(dis[-1]+1)