def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    
    # 이진탐색 , left>right가 되는 순간 이진탐색 종료
    while left<=right:
        mid = (left+right)//2
        count = 0 # mid 시간 동안 최대로 심사할 수 있는 인원
        for time in times:
            count += mid//time
            
            if count >= n: # n명을 심사할 수 있는지에 관심이 있으므로 for문 탈출
                break
            
        # 심사볼수 있는 인원이 n명 이상이다 --> 시간이 과잉되었다 --> max 시간 감소
        if count >=n:
            answer = mid
            right = mid-1
        # 심사볼수 있는 인원이 n명 미만이다 --> 시간이 모자르다 --> min 시간 증가
        else:
            left = mid+1
    return answer