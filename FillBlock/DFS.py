from time import perf_counter

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
step = 0 

def dfs_solver(start, white_cells, N):
    global step
    step = 0  # reset mỗi lần gọi
    t0 = perf_counter()

    white = set(tuple(c) for c in white_cells)
    s = tuple(start)
    if s not in white:
        return None

    target_len = len(white)
    path = [s]
    visited = {s}

    def backtrack(u):
        global step
        step += 1  # mở rộng 1 node
        if len(path) == target_len:
            return True
        x, y = u
        for k in range(4):
            v = (x + dx[k], y + dy[k])
            if 0 <= v[0] < N and 0 <= v[1] < N and v in white and v not in visited:
                visited.add(v)
                path.append(v)
                if backtrack(v):
                    return True
                path.pop()
                visited.remove(v)
        return False

    if backtrack(path[0]):
        return path, step
    return None
