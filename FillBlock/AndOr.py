from time import perf_counter

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
step = 0

def and_or_search(start_pos, white_cells, N):
    global step
    t0 = perf_counter()
    white_set = set(tuple(c) for c in white_cells)
    s = tuple(start_pos)
    if s not in white_set:
        return None

    cache = {}

    def subproblem(cur, remaining_fs):
        global step
        step += 1
        key = (cur, remaining_fs)
        if not remaining_fs:
            return [cur]
        if key in cache:
            return cache[key]

        remaining = set(remaining_fs)

        x, y = cur
        cand = []
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                nb = (nx, ny)
                if nb in remaining:
                    # bậc nhỏ ưu tiên
                    c = 0
                    xx, yy = nb
                    for t in range(4):
                        rx, ry = xx + dx[t], yy + dy[t]
                        if 0 <= rx < N and 0 <= ry < N:
                            nb2 = (rx, ry)
                            if nb2 in remaining and nb2 != cur:
                                c += 1
                    cand.append((c, nb))
        cand.sort(key=lambda z: z[0])

        for _, nb in cand:
            res = subproblem(nb, frozenset(remaining - {nb}))
            if res is not None:
                cache[key] = [cur] + res
                return cache[key]
        cache[key] = None
        return None

    remaining = set(white_set)
    remaining.discard(s)
    path = subproblem(s, frozenset(remaining))
    if path is not None:
        return path, step
    return None
