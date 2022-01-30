cases = [["119", "97674223", "1195524421"], ["123","456","789"], ["12","123","1235","567","88"]]


def solution(phone_book) :
    for i in range(len(phone_book)) :
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True



print(solution(cases[2]))