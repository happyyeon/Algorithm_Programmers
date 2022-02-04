import math
from collections import deque

def solution(board):
    def bfs(start):
        # table[y][x] = �ش� ��ġ�� �����ϴ� �ּڰ�.
        table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]
        # ���� ����. �� - 0, ���� - 1, �Ʒ� = 2, ������ = 3
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        queue = deque([start])
        
        # ó�� ��ġ�� ��� = 0
        table[0][0] = 0
        while queue:
            # y��ǥ, x��ǥ, ���, �������
            y, x, cost, head = queue.popleft()
            for idx, (dy, dx) in enumerate(dirs):
                ny, nx = y + dy, x + dx
                # �������� ���� ������ ��ġ�ϸ� + 100, �ٸ��� ��ȯ��� 500 + ������ 100 = 600
                n_cost = cost + 600 if idx != head else cost + 100
                # board[y][x] == 0 : ������⿡ ���� ����. table[ny][nx] > n_cost : ���� ��ǥ�� �ּڰ����� ������� ����� ���� ���
                if 0 <= ny < len(board) and 0 <= nx < len(board) and board[ny][nx] == 0 and table[ny][nx] > n_cost:
                    # table ��ǥ ������Ʈ.
                    table[ny][nx] = n_cost
                    queue.append((ny, nx, n_cost, idx))
        return table[-1][-1]
    return min(bfs((0,0,0,2)), bfs((0,0,0,3)))