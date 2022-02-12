import sys
sys.stdin = open('input.txt', 'r')

N,M = map(int, input().split())
board = []
for _ in range(N) :
    board.append(input())

w_case = "WB"*4 + "BW"*4
b_case = "BW"*4 + "WB"*4
min = 2174000
cnt_1 = 0
cnt_2 = 0

for r in range(N-7):
    for c in range(M-7):

        cnt_1 = 0
        cnt_2 = 0
        sector = ""

        for row in board[r:r+8] :
            sector += row[c:c+8]
            if len(sector) == 16:
                for i in range(16) :
                    if sector[i] != w_case[i]:
                        cnt_1 += 1
                    elif sector[i] != b_case[i] :
                        cnt_2 += 1
                sector = ""

        if cnt_1 <= cnt_2 and cnt_1 < min :
            min = cnt_1
        elif cnt_2 < cnt_1 and cnt_2 < min :
            min = cnt_2

print(min)
