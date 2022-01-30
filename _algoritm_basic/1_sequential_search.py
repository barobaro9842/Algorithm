import time

def sequential_search(n, target, array):
    for i in range(n) : # length of array
        if array[i] == target :
            return i+1




for max_num in [10**i for i in range(1,8)] :
    array = [i for i in range(1,max_num)]
    n = len(array)
    target = max_num - 1

    tic = time.time()
    res = sequential_search(n,target, array)
    toc = time.time()
    print('max num :',max_num , end=' && ')
    print('time :', toc - tic, 's')

#O(n)의 시간복잡도로, 데이터 증가분만큼 시간이 그대로 증가, 10^9승부터 계산 버거움 약 1분 소요