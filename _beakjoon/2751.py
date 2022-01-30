#quick sort는 최악의 경우 n^2이 될 수 있다.
#nlogn을 보장하는 방법은?

#병합정렬 또는 힙정렬 사용 필요
from heapq import *

n = int(input())
a = []
for i in range(n) :
    x = int(input())
    
