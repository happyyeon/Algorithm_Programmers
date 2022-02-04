def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    
    # ����Ž�� , left>right�� �Ǵ� ���� ����Ž�� ����
    while left<=right:
        mid = (left+right)//2
        count = 0 # mid �ð� ���� �ִ�� �ɻ��� �� �ִ� �ο�
        for time in times:
            count += mid//time
            
            if count >= n: # n���� �ɻ��� �� �ִ����� ������ �����Ƿ� for�� Ż��
                break
            
        # �ɻ纼�� �ִ� �ο��� n�� �̻��̴� --> �ð��� ���׵Ǿ��� --> max �ð� ����
        if count >=n:
            answer = mid
            right = mid-1
        # �ɻ纼�� �ִ� �ο��� n�� �̸��̴� --> �ð��� ���ڸ��� --> min �ð� ����
        else:
            left = mid+1
    return answer