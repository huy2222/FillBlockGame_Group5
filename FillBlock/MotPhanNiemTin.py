dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def MotphanNiemtin(start_pos, domain, N, end_pos):
    step = 0
    wall = []  # vat can
    path = [start_pos]  # nhung o co the di duoc
    stack = [[start_pos]]
    while stack:
        state = stack.pop()
        step += 1
        if len(state) == len(domain) and state[-1] == end_pos:
            return state, step
        # di chuyen
        x, y = state[-1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            next_pos = (nx, ny)
            if 0 <= nx < N and 0 <= ny < N:
                if next_pos not in domain and next_pos not in wall:
                    wall.append(next_pos)
                if next_pos in domain and next_pos not in state:
                    if next_pos not in path:
                        path.append(next_pos)
                    new_state = state + [next_pos]
                    stack.append(new_state)
    return None, step






