from itertools import permutations

# 두 문자열 리스트의 비교
def check(a,b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if b[i] == "*":
                continue
            if a[i] != b[i]:
                return False
        return True
            

def solution(user_id, banned_id):
    answer = []
    
    # 모든 user id를 비교한 후 아래 조건에 부합되는 id쌍들만 answer에 추가한다.
    for i in permutations(user_id,len(banned_id)):
        count = 0
        for a,b in zip(i,banned_id):
            if check(a,b):
                count += 1
        # 경우의 수를 따지기 위하여
        if count == len(banned_id) and set(i) not in answer:
            # 제재 아이디 목록 생성
            answer.append(set(i))
    return len(answer)