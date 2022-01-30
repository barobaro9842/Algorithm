graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["peggy"] = []
graph["jonny"] = []





def person_is_seller(person) :
    if person == 'peggy':
        return True

def search_mango_dealer(person):
    from collections import deque
    
    search_queue = deque() #큐 생성
    search_queue += graph["you"]  #큐에 you에 연결된 노드 추가
    searched = [] #이미 확인한 사람을 제외하기 위함 (서로를 가리키는 노드가 있으면 무한 반복)
    while search_queue :
        person = search_queue.popleft() #가장 첫번째 노드 확인 pop
        if not person in searched : #이미 검사한 사람이면 건너 뜀
            if person_is_seller(person) : # 그 사람이 셀러가 맞나
                print(f'{person} is a mango seller!')
                return True # 종료

            else: #아니면
                search_queue += graph[person] # 그 사람과 연결된 노드를 큐에 추가
                searched.append(person)
    
    return False

print(search_mango_dealer("you"))


# from collections import deque
# queue = deque()
# queue += graph["you"]
# a = queue.popleft()
# print(a)

