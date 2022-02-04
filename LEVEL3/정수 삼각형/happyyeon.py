# integer triangle
#

def solution(triangle):
    length = len(triangle)
    # dp[i][j]: max sum route in (i,j) of triangle
    for i in range(1,length):
        for j in range(i+1):
            if j == 0: # triangle left
                triangle[i][j] += triangle[i-1][j]
            elif j == i: # triangle right
                triangle[i][j] += triangle[i-1][j-1]
            else: # triangle middle
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])