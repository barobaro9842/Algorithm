clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

from functools import reduce

def solution(clothes) :
    dic = {}
    for cloth in clothes :
        if dic.get(cloth[1]):
            dic[cloth[1]] += 1
        else :
            dic[cloth[1]] = 1
    mix = list(dic.values())
    mix = list(map(lambda x : x+1, mix))
    
    answer = reduce(lambda x, y : x * y, mix)
        
    return answer

print(solution(clothes))