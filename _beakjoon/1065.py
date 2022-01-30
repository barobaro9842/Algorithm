n = 1000
cnt = 0

def ed(n):
    global cnt
    if n < 100 :
        return n
    else :
        for x in range(111, n+1):
            n = str(x)
            dif = int(n[1]) - int(n[0])
            for i in range(1, len(n)) :
                if dif != int(n[i]) - int(n[i-1]):
                    break
            else : cnt += 1
        return 99 + cnt


print(ed(n))