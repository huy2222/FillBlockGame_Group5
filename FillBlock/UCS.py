from queue import PriorityQueue

def is_valid(white_cells, N, path, pos):
    if (
        pos not in path
        and pos in white_cells
        and 0 <= pos[0] < N
        and 0 <= pos[1] < N
    ):
        return True
    return False

def calculate_cost(path, white_cells, n):
    cost = 0
    np = path[-1]
    path_set = set(path[:-1])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        x = np[0] + dx[i]
        y = np[1] + dy[i]
        if (x, y) in white_cells and (x, y) not in path_set:
            cost += 1
    if cost == 0 and (len(path) < len(white_cells)):
        return 1000
    else:
        return cost  # chi phí = số bước đi

def generate_next_state(white_cells, N, path):
    np = path[-1]
    next_paths = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        x = np[0] + dx[i]
        y = np[1] + dy[i]
        if is_valid(white_cells, N, path, (x, y)):
            new_path = path + [(x, y)]
            cost = calculate_cost(new_path, white_cells, N)
            next_paths.append((cost, new_path))
    return next_paths

def ucs(start_pos, white_cells, N):
    pq = PriorityQueue()
    pq.put((calculate_cost([start_pos], white_cells, N), [start_pos]))
    step = 0

    while not pq.empty():
        cost, path = pq.get()
        step += 1

        # nếu đi qua hết white_cells thì trả về path
        if len(path) == len(white_cells):
            return path, step

        for next_cost, next_path in generate_next_state(white_cells, N, path):
            pq.put((next_cost, next_path))

    return None, step
