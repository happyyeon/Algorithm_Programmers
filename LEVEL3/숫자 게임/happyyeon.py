# -*-encoding:utf-8 -*-
# 숫자 게임
### 효율성 테스트 미통과 코드
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

#1. max(A)를 이길 수 있는 B가 있다면 승점 챙기기
#2. max(A)를 이길 수 없다면 min(B)를 버림으로써 이득보기

def solution(A, B):
    win_point = 0
    # A,B 내림차순 정렬
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