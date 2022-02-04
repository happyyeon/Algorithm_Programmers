from itertools import permutations

# ������ �� �� �Ƿε��� ��� count�� ����
def count_dungeon(k,dungeons):
    count = 0
    for i in range(len(dungeons)): # ���� ������� �ݺ�
        if dungeons[i][0] > k: # �ּ� �ʿ� �Ƿε�
            return count # �߰� �������� �Ƿε� ������ count ���� �� Ż��
        k -= dungeons[i][1] # �Ҹ� �Ƿε�
        count += 1
    return count # ��� ������ �� ������ �� ���� count ����
    

def solution(k, dungeons):
    lst_count = []
    for order in permutations(dungeons): # dungeons�� ��� ���� �� �� ���� ������ ���Ͽ�
        lst_count.append(count_dungeon(k,order))
        
    return max(lst_count)