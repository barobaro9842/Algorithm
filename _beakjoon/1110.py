N = 55
M = N
cnt = 0
def sum_digit(N,M,cnt):
    a = M // 10
    b = M % 10
    c = b*10 + ((a+b) % 10)
    cnt += 1
    if c == N :
        return cnt
    else :
        return sum_digit(N,c,cnt)

a = sum_digit(N,M,cnt)
print(a)