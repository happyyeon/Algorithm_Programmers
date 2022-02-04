import sys
    
def solution(n, s, a, b, fares):    
    INF = sys.maxsize
    answer = INF
    cost = [[INF]*(n+1) for _ in range(n+1)]
    def floyd_warshall(n):
        for k in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if i==j:
                        cost[i][j] = 0
                    else:
                        cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])
    for i,j,c in fares:
        cost[i][j] = c
        cost[j][i] = c
    floyd_warshall(n)
    
    for i in range(1,n+1):
        answer = min(answer, cost[s][i]+cost[i][a]+cost[i][b])
    
    return answer