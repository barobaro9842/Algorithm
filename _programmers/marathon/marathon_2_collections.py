import collections
from functools import partial

participant = ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]

# Counter 객체는 값의 빈도를 반환
# Dictionary 간 마이너스 연산
answer = collections.Counter(participant) - collections.Counter(completion)

print(list(answer.keys())[0])