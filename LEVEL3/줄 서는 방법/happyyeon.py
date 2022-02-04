# 팩토리얼
def factorial(num):
    # base case
    dp = [1]*(num+1)
    # 팩토리얼 dp 생성
    for i in range(2,num+1):
        dp[i] = i*dp[i-1]
    return dp[num]
    
def solution(n, k):
    # 총 인원들의 순열
    lst = [0]*n
    for i in range(n):
        lst[i] = i+1
    answer = []
    while n!=0:
    # answer 리스트에 배치될 사람의 lst 리스트 내의 인덱스
        lst_idx = (k-1)//factorial(n-1)
        answer.append(lst[lst_idx])
        lst.pop(lst_idx)
        # k update
        k = k%factorial(n-1)
      
        n -= 1
    return answer