dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
step = 0
def ForwardChecking(state, domain, N):
    global step
    step+=1
    if len(domain) == 1:
        return state, step
    x, y = state[-1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            next_pos = (nx, ny)
            if next_pos in domain and next_pos not in state:
                new_state = state.copy()
                new_state.append(next_pos)

                new_domain = domain.copy()
                new_domain.remove(next_pos)
                res = ForwardChecking(new_state, new_domain, N)
                if res is not None:
                    return res
    return None

