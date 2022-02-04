import heapq

def solution(n, works):
    # 예외 처리
    if sum(works)<=n:
        return 0
    
    # min heap을 max heap으로 변환해주기 위해
    works = [-w for w in works]
    # works 리스트를 heap으로 만들어준다
    heapq.heapify(works)
    
    for i in range(n):
        i = heapq.heappop(works) # heap에서 최소값 빼줌(원래 리스트의 최대)
        i += 1 # 1 더해줌 (원래 값에서 -1)
        heapq.heappush(works,i) # heap update
    
    return sum([w**2 for w in works])