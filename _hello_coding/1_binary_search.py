def binary_search(arr, item):
    L = 0
    H = len(arr) - 1

    while L <= H :
        mid = int((L + H) / 2)
        guess = arr[mid]

        if guess == item :
            return mid
        if guess > item :
            H = mid - 1
        else :
            L = mid + 1
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list,3))
print(binary_search(my_list,-1))