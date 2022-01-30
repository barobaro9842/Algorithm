n = 3
m = 16

ck = [0] * (m+2)

ck[1] = 1
ck[0] = 1

for i in range(2, m//2+1) :
    if ck[i] == 0:
        for j in range(i*2,m+1,i):
            ck[j] = 1
    else :
        continue

for i in range(n,m+1):
    if ck[i] == 0 :
        print(i)