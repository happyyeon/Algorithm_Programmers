# Network
#

# find network by using DFS
def dfs(computers,i,check):
    check[i] = 1 # mark visiting

    for j in range(len(computers)):
        if (i != j) and (check[j] == 0) and computers[i][j] == 1:
            check = dfs(computers,j,check)
    return check

def solution(n, computers):
    answer = 0
    check = [0]*n # check for visiting computer
    for i in range(n):
        if check[i] == 0:
            dfs(computers,i,check)
            answer += 1
    return answer