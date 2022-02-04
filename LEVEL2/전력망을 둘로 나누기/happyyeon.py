import sys
sys.setrecursionlimit(10**6)

def solution(n, wires):
    answer = float('inf')
    
    def dfs(cur,count):
        visited[cur] = 1
        count += 1
        
        for i in graph[cur]:
            if not visited[i]:
                count = dfs(i,count)
        return count
    
    for i in range(n-1):
        graph = [[] for _ in range(n+1)] 
        
        # i만 빼고 다 연결
        for idx,wire in enumerate(wires):
            if idx == i:
                continue
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
            
        visited = [0]*(n+1)
        area = []
        
        for node in range(1,n+1):
            if not visited[node]:
                area.append(dfs(node,0))
        
        answer = min(answer,abs(area[0]-area[1]))

    return answer