from time import perf_counter
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
step = 0

def ac3_path(start_pos, white_cells, N):
    global step
    t0 = perf_counter()
    white_set = set(tuple(c) for c in white_cells)
    s = tuple(start_pos)
    if s not in white_set:
        return None

    K = len(white_set)
    domains = [set(white_set) for _ in range(K)]
    domains[0] = {s}

    q = deque()
    for i in range(K - 1):
        q.append((i, i + 1))
        q.append((i + 1, i))

    def revise(xi, xj):
        nonlocal domains
        removed = False
        Di = domains[xi]
        Dj = domains[xj]
        new_Di = set()
        for vi in Di:
            ok = False
            if abs(xi - xj) == 1:
                for vj in Dj:
                    step_inc = True
                    if abs(vi[0] - vj[0]) + abs(vi[1] - vj[1]) == 1:
                        ok = True
                        break
            else:
                ok = True
            if ok:
                new_Di.add(vi)
            else:
                removed = True
        if removed:
            domains[xi] = new_Di
        return removed

    while q:
        xi, xj = q.popleft()
        step += 1
        if revise(xi, xj):
            if not domains[xi]:
                return None
            if xi - 1 >= 0:
                q.append((xi - 1, xi))
            if xi + 1 < K:
                q.append((xi + 1, xi))

    assignment = [None] * K
    used = set()

    def deg(cell):
        x, y = cell
        c = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                nb = (nx, ny)
                if (nb in white_set) and (nb not in used):
                    c += 1
        return c

    def backtrack(i):
        global step
        if i == K:
            return True
        Di = list(domains[i])
        Di.sort(key=lambda c: deg(c))
        for v in Di:
            step += 1
            if v in used:
                continue
            if i > 0:
                px, py = assignment[i - 1]
                if abs(px - v[0]) + abs(py - v[1]) != 1:
                    continue
            assignment[i] = v
            used.add(v)
            if i + 1 < K:
                ok_next = False
                for u in domains[i + 1]:
                    if (u not in used) and (abs(u[0] - v[0]) + abs(u[1] - v[1]) == 1):
                        ok_next = True
                        break
                if not ok_next:
                    used.remove(v)
                    assignment[i] = None
                    continue
            if backtrack(i + 1):
                return True
            used.remove(v)
            assignment[i] = None
        return False

    if backtrack(0):
        return assignment, step
    return None
