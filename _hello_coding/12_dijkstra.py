graph = {} #전체 테이블
graph["start"] = {} #시작점
graph["start"]["a"] = 6 #노드 a와 가중치 6
graph["start"]["b"] = 2 #노드 b와 가중치 2
# {start : {a : 6 , b : 2}} 이와 같은 형태

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
# {start : {a : 6, b : 2}, a : {fin : 1}, b : {a : 3, fin : 5}, fin : {}}

# 변화하는 비용 기록
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity # 아직 알 수 없음
# {a:6, b:2, fin:inf}

# 부모노드 기록 테이블 (최종 경로 탐색)
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None # 아직 정해지지 않음

#이미 처리한 정점 추적
processed = []



def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs :
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node



node = find_lowest_cost_node(costs) # 아직 처리하지 않은 가장 싼 정점을 찾는다.

cnt = 0
while node is not None : # 모든 정점을 처리하면 반복문 종료
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): #모든 이웃에 대해 반복한다.
        new_cost = cost + neighbors[n] #기존 비용과 이웃의 비용을 합한다.
        if costs[n] > new_cost: # 기존 비용보다 이 정점을 지나는 것이 가격이 더 싸다면
            costs[n] = new_cost # 이 정점을 지나는 것으로 비용을 업데이트한다.
            parents[n] = node # 부모를 이 정점으로 설정
    
    processed.append(node)

    node = find_lowest_cost_node(costs) #다음으로 처리할 정점을 찾아 반복

print(parents)
print(costs)
print(processed)