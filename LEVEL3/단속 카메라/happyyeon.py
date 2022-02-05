# 단속 카메라

def solution(routes):
    if len(routes) == 1:
        return 1
    cam = 1 # 최소 카메라 개수(정답)
    # 그리디 알고리즘을 위하여 오름차순 정렬
    routes.sort(key=lambda x:x[1])
    location_cam = routes[0][1]
    # 그리디 알고리즘
    for i in range(1,len(routes)):
        start = routes[i][0]
        if routes[i][0] <= location_cam:
            continue
        cam += 1
        location_cam = routes[i][1]
    return cam