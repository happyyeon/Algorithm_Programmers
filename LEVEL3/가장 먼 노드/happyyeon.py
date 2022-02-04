from collections import deque
def solution(n, edge):
    graph = {} 
    visited = [0]*n # 방문한 노드
    q = deque()
    for e in edge:
        graph[e[0]] = graph.get(e[0],[]) + [e[1]]
        graph[e[1]] = graph.get(e[1],[]) + [e[0]]
    
    q.append(1) # 큐에 1을 넣고 시작
    visited[0] = 1 # 방문 노드 초기화
    while q:
        nodes = len(q)
    # 1에 연결된 "3,2"를 큐에 넣고 pop
    # "3,2"를 pop하며 각각 연결된 노드들 append
        for _ in range(nodes):
            for node in graph[q.popleft()]:
                if visited[node-1] == 0: # 방문 안했다면
                        visited[node-1] = 1 # 방문 마킹하고
                        q.append(node) # 큐에 해당노드 추가

    return nodes