from time import perf_counter
import random

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
step = 0

def hill_climbing_path(start_pos, white_cells, N, max_restarts=10):
    global step
    t0 = perf_counter()
    white_set = set(tuple(c) for c in white_cells)
    s0 = tuple(start_pos)
    if s0 not in white_set:
        return None

    # kiểm tra liên thông
    def is_connected():
        global step
        any_cell = next(iter(white_set))
        q = [any_cell]
        seen = {any_cell}
        while q:
            u = q.pop()
            step += 1
            x, y = u
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    nb = (nx, ny)
                    if (nb in white_set) and (nb not in seen):
                        seen.add(nb); q.append(nb)
        return len(seen) == len(white_set)

    if not is_connected():
        return None

    def degree(cell, used):
        x, y = cell
        c = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                nb = (nx, ny)
                if (nb in white_set) and (nb not in used):
                    c += 1
        return c

    def greedy(seed):
        global step
        used = {seed}
        path = [seed]
        target = len(white_set)
        while len(path) < target:
            step += 1
            x, y = path[-1]
            cands = []
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    nb = (nx, ny)
                    if (nb in white_set) and (nb not in used):
                        cands.append(nb)
            if not cands:
                return None
            # Warnsdorff: chọn bậc nhỏ nhất
            scored = [(degree(nb, used), nb) for nb in cands]
            best_d = min(d for d, _ in scored)
            bests = [nb for d, nb in scored if d == best_d]
            if len(bests) > 1:
                # tie-break nhìn trước một vòng
                look = []
                for nb in bests:
                    tmp_used = used | {nb}
                    s2 = c2 = 0
                    xx, yy = nb
                    for t in range(4):
                        rx, ry = xx + dx[t], yy + dy[t]
                        if 0 <= rx < N and 0 <= ry < N:
                            nb2 = (rx, ry)
                            if (nb2 in white_set) and (nb2 not in tmp_used):
                                s2 += degree(nb2, tmp_used)
                                c2 += 1
                    look.append(((s2 / c2) if c2 else 0, nb))
                look.sort(key=lambda z: z[0])
                nb = look[0][1]
            else:
                nb = bests[0]
            used.add(nb); path.append(nb)
        return path

    seeds = [s0]
    x0, y0 = s0
    neighs = []
    for k in range(4):
        nx, ny = x0 + dx[k], y0 + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            nb = (nx, ny)
            if nb in white_set:
                neighs.append(nb)
    neighs.sort(key=lambda c: degree(c, set()))
    seeds += neighs[:max(1, max_restarts // 2)]

    tried = set()
    for seed in seeds:
        if seed in tried:
            continue
        tried.add(seed)
        res = greedy(seed)
        if res is not None and len(res) == len(white_set):
            if res[0] != s0 and abs(res[0][0] - s0[0]) + abs(res[0][1] - s0[1]) == 1:
                res = [s0] + res
            return res, step

    return None
