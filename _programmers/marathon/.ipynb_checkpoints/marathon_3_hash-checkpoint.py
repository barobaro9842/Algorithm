participant = ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]

answer = ''
temp = 0
dic = {}
#hash를 이용하면 같은 값도 다른 hash로 판별한다.

for part in participant:
    dic[hash(part)] = part
    temp += hash(part)

for comp in completion :
    temp -= hash(comp)

answer = dic[temp]
print(answer)
