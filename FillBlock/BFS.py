from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
from collections import deque

def BFS(start_pos, white_cells, N):
    step = 0
    path = deque()
    path.appendleft([start_pos])
    while path:
        state = path.popleft()
        step += 1
        if len(state) == len(white_cells):  
            return state, step

        x, y = state[-1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            next_pos = (nx, ny)
            if 0 <= nx < N and 0 <= ny < N:
                if next_pos in white_cells and next_pos not in state:
                    new_state = state + [next_pos]
                    path.appendleft(new_state)

    return None, step
