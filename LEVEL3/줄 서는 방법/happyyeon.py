# ���丮��
def factorial(num):
    # base case
    dp = [1]*(num+1)
    # ���丮�� dp ����
    for i in range(2,num+1):
        dp[i] = i*dp[i-1]
    return dp[num]
    
def solution(n, k):
    # �� �ο����� ����
    lst = [0]*n
    for i in range(n):
        lst[i] = i+1
    answer = []
    while n!=0:
    # answer ����Ʈ�� ��ġ�� ����� lst ����Ʈ ���� �ε���
        lst_idx = (k-1)//factorial(n-1)
        answer.append(lst[lst_idx])
        lst.pop(lst_idx)
        # k update
        k = k%factorial(n-1)
      
        n -= 1
    return answer