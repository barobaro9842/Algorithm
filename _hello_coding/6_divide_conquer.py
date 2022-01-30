def sum(arr) :
    total = 0
    for x in arr :
        total += x
    return total

print(sum([1,2,3,4]))


def sum_2(arr):
    if len(arr) >= 1:
        return arr[0] + sum_2(arr[1:])
    
print(sum([1,2,3,4]))