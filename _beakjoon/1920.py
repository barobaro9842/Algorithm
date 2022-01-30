n = [4,1,5,2,3]
m = [1,3,7,9,5]

n.sort()

def bin_search(x):
    global n
    s = 0
    e = len(n)-1
    while s<=e :
        mid = (s + e) // 2
        if n[mid] == x :
            print(n[mid])
            return 1
        elif n[mid] > x :
            e = mid-1
        elif n[mid] < x :
            s = mid+1
    return 0

for x in m :
    print(bin_search(x))