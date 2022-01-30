clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
from functools import reduce

def solution(clothes):
    from collections import Counter
    

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y : x*(y+1), cnt.values(), 1) -1

    return cnt


print(solution(clothes))

#1 = initial
print(reduce(lambda x,y : x*(y+1), [2,3,4], 1) - 1)