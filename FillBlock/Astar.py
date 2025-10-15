from time import perf_counter
import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
step = 0 

def astar_solver(start, white_cells, N):
    global step
    step = 0  # reset
    t0 = perf_counter()

    white = set(tuple(c) for c in white_cells)
    s = tuple(start)
    if s not in white:
        return None

    target_len = len(white)

    def h(count_visited):
        return target_len - count_visited

    g0 = 1
    v0 = frozenset([s])
    pq = []
    heapq.heappush(pq, (g0 + h(len(v0)), g0, [s], v0, s))

    best_g = {}

    while pq:
        f, g, path, visited, u = heapq.heappop(pq)
        step += 1 
        if len(path) == target_len:
            return path, step

        key = (u, visited)
        if key in best_g and best_g[key] <= g:
            continue
        best_g[key] = g

        x, y = u
        for k in range(4):
            v = (x + dx[k], y + dy[k])
            if 0 <= v[0] < N and 0 <= v[1] < N and v in white and v not in visited:
                new_path = path + [v]
                new_visited = visited | {v}
                g2 = g + 1
                f2 = g2 + h(len(new_visited))
                heapq.heappush(pq, (f2, g2, new_path, new_visited, v))

    return None
