from collections import deque
def solution(n, edge):
    graph = {} 
    visited = [0]*n # �湮�� ���
    q = deque()
    for e in edge:
        graph[e[0]] = graph.get(e[0],[]) + [e[1]]
        graph[e[1]] = graph.get(e[1],[]) + [e[0]]
    
    q.append(1) # ť�� 1�� �ְ� ����
    visited[0] = 1 # �湮 ��� �ʱ�ȭ
    while q:
        nodes = len(q)
    # 1�� ����� "3,2"�� ť�� �ְ� pop
    # "3,2"�� pop�ϸ� ���� ����� ���� append
        for _ in range(nodes):
            for node in graph[q.popleft()]:
                if visited[node-1] == 0: # �湮 ���ߴٸ�
                        visited[node-1] = 1 # �湮 ��ŷ�ϰ�
                        q.append(node) # ť�� �ش��� �߰�

    return nodes