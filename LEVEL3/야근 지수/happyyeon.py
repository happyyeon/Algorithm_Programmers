import heapq

def solution(n, works):
    # ���� ó��
    if sum(works)<=n:
        return 0
    
    # min heap�� max heap���� ��ȯ���ֱ� ����
    works = [-w for w in works]
    # works ����Ʈ�� heap���� ������ش�
    heapq.heapify(works)
    
    for i in range(n):
        i = heapq.heappop(works) # heap���� �ּҰ� ����(���� ����Ʈ�� �ִ�)
        i += 1 # 1 ������ (���� ������ -1)
        heapq.heappush(works,i) # heap update
    
    return sum([w**2 for w in works])