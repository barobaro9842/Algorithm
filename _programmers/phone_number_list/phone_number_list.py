cases = [["119", "97674223", "1195524421"], ["123","456","789"], ["12","123","1235","567","88"]]

def sol(phone_book):
    hash_map = {}
    answer = True
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp =""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return hash_map
        
if "119" in sol(cases[0]) :
    print(1)