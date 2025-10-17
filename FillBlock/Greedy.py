from queue import PriorityQueue
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def PathCostGreedy(question, stateNow):
    x, y = stateNow[-1]
    remaining = []
    for (wx, wy) in question:
        if (wx, wy) not in stateNow:
            remaining.append(abs(x-wx)+abs(y - wy))
    return min(remaining) if remaining else 0
def Greedy(start_pos, white_cells, N):
    step = 0
    path = PriorityQueue()
    path.put((PathCostGreedy(white_cells, [start_pos]), [start_pos]))
    while path:
        cost, state = path.get()
        step+=1
        if len(state) == len(white_cells):  # đi qua hết white_cells
            return state, step
        x, y = state[-1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            next_pos = (nx, ny)
            if 0 <= nx < N and 0 <= ny < N:
                if next_pos in white_cells and next_pos not in state:
                    new_state = state + [next_pos]
                    new_cost = PathCostGreedy(white_cells, new_state)
                    path.put((new_cost, new_state))
    return None, step