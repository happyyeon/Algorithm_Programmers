# �ܼ� ī�޶�

def solution(routes):
    if len(routes) == 1:
        return 1
    cam = 1 # �ּ� ī�޶� ����(����)
    # �׸��� �˰����� ���Ͽ� �������� ����
    routes.sort(key=lambda x:x[1])
    location_cam = routes[0][1]
    # �׸��� �˰���
    for i in range(1,len(routes)):
        start = routes[i][0]
        if routes[i][0] <= location_cam:
            continue
        cam += 1
        location_cam = routes[i][1]
    return cam