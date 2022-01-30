import time

# def binary_search(target, array):
#     m_index = int(round(len(array) / 2 + 0.5))
#     if m_index >= 1:
#         m = array[m_index]
#     else:
#         return None

#     if m == target :
#         return m_index
#     elif m > target :
#         return binary_search(target, array[:m_index+1])
#     else :
#         return binary_search(target, array[m_index+1:])

def binary_search(target, array):
    m = -1
    l_a = len(array)
    s = 0
    e = l_a-1

    while s <= e :
        m = (s+e) // 2
        if array[m] == target:
            return m+1
        elif array[m] > target:
            e = m-1
        else :
            s = m-1
    return None




for max_num in [10**i for i in range(1,9)] :
    array = [i*2 for i in range(1,max_num)]
    n = len(array)
    
    target = 6

    tic = time.time()
    res = binary_search(target, array)
    toc = time.time()
    print('max num :',max_num , end=' && ')
    print('time :', toc - tic, 's', end=' && ')
    print('answer : ', res)
