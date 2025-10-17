from time import perf_counter

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
step = 0

def hill_climbing_path(start_pos, white_cells, N, max_restarts=0):
    global step
    step = 0
    t0 = perf_counter()

    white = set(map(tuple, white_cells))
    s0 = tuple(start_pos)
    if s0 not in white:
        return None

    def degree(cell, used):
        x, y = cell
        c = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            nb = (nx, ny)
            if 0 <= nx < N and 0 <= ny < N and nb in white and nb not in used:
                c += 1
        return c

    def neighbors(cell, used):
        x, y = cell
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            nb = (nx, ny)
            if 0 <= nx < N and 0 <= ny < N and nb in white and nb not in used:
                yield nb

    used = {s0}
    path = [s0]

    while True:
        step += 1
        u = path[-1]
        cands = list(neighbors(u, used))
        if not cands:
            break

        best_nb = min(cands, key=lambda v: (degree(v, used), v[0], v[1]))
        used.add(best_nb)
        path.append(best_nb)

    return path, step