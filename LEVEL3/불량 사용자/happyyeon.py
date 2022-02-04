from itertools import permutations

# �� ���ڿ� ����Ʈ�� ��
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
    
    # ��� user id�� ���� �� �Ʒ� ���ǿ� ���յǴ� id�ֵ鸸 answer�� �߰��Ѵ�.
    for i in permutations(user_id,len(banned_id)):
        count = 0
        for a,b in zip(i,banned_id):
            if check(a,b):
                count += 1
        # ����� ���� ������ ���Ͽ�
        if count == len(banned_id) and set(i) not in answer:
            # ���� ���̵� ��� ����
            answer.append(set(i))
    return len(answer)