# ids.py
step = 0
def is_valid(pos, visited, white_cells, N):
    x, y = pos
    if not (0 <= x < N and 0 <= y < N):
        return False
    if pos in visited:
        return False
    if pos not in white_cells:
        return False
    return True

def generate_state(path, white_cells, N):
    if not path:
        return []

    x, y = path[-1]
    visited = set(path)
    moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # trái, lên, phải, xuống
    next_paths = []

    for dx, dy in moves:
        new_pos = (x + dx, y + dy)
        if is_valid(new_pos, visited, white_cells, N):
            next_paths.append(path + [new_pos])
    return next_paths

def DLS(path, depth_limit, white_cells, N):
    global step
    step += 1
    if len(path) == len(white_cells):
        return path, step
    if depth_limit == 0:
        return None

    for new_path in generate_state(path, white_cells, N):
        result = DLS(new_path, depth_limit - 1, white_cells, N)
        if result:
            return result
    return None

def run_dls_model(start_pos, white_cells, N):
    global step
    step = 0
    depth = len(white_cells)
    result = DLS([start_pos], depth, set(white_cells), N)
    if result:
        return result
