from itertools import permutations

# 던전을 돌 때 피로도를 깎고 count를 증가
def count_dungeon(k,dungeons):
    count = 0
    for i in range(len(dungeons)): # 던전 순서대로 반복
        if dungeons[i][0] > k: # 최소 필요 피로도
            return count # 중간 던전에서 피로도 소진시 count 리턴 후 탈출
        k -= dungeons[i][1] # 소모 피로도
        count += 1
    return count # 모든 던전을 다 돌았을 시 최종 count 리턴
    

def solution(k, dungeons):
    lst_count = []
    for order in permutations(dungeons): # dungeons의 모든 순서 중 한 개의 순서에 대하여
        lst_count.append(count_dungeon(k,order))
        
    return max(lst_count)