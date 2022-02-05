# -*-encoding:utf-8 -*-
# ���� ����
### ȿ���� �׽�Ʈ ����� �ڵ�
# def solution(A, B):
#     answer = 0
#     lst_answer = [0]*len(A)
#     for i in range(len(A)):
#         next = max(A)
#         idx = A.index(next)
#         new_B = [b for b in B if b>next]
#         if new_B:
#             answer += 1
#             B[B.index(min(new_B))] = 0
#             A[idx] = 0
#         else:
#             A[idx] = 0
#     return answer

#1. max(A)�� �̱� �� �ִ� B�� �ִٸ� ���� ì���
#2. max(A)�� �̱� �� ���ٸ� min(B)�� �������ν� �̵溸��

def solution(A, B):
    win_point = 0
    # A,B �������� ����
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    while B:
        if B[0]>A[0]:
            win_point += 1
            B.pop(0)
            A.pop(0)
        else:
            B.pop(-1)
            A.pop(0)
    return win_point

A = [5,1,3,7]
B = [2,2,6,8]
print(solution(A,B))