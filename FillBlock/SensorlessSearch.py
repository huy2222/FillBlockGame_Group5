# SensorlessSearch.py

from collections import deque

def move(pos, action, N, white_cells):
    x, y = pos[-1]

    if action == "Up":
        nx, ny = x-1, y
    elif action == "Down":
        nx, ny = x+1, y
    elif action == "Left":
        nx, ny = x, y-1
    elif action == "Right":
        nx, ny = x, y+1
    else:
        nx, ny = x, y

    # kiểm tra ngoài lưới
    if not (0 <= nx < N and 0 <= ny < N):
        return None
    # kiểm tra ô trắng
    if (nx, ny) not in white_cells:
        return None
    if (nx, ny) in pos:
        return None

    # Bỏ kiểm tra đi lại, cho phép quay lại
    return pos + [(nx, ny)]

def apply_action_to_belief(belief, action, N, white_cells):
    new_belief = set()
    for path in belief:
        new_path = move(list(path), action, N, white_cells)
        if new_path is not None:
            new_belief.add(tuple(new_path))  # tuple để hashable
    if new_belief:
        return frozenset(new_belief)
    return None

def goal_test_path(belief, white_cells):
    """
    Trả về path duy nhất đạt mục tiêu, hoặc None nếu chưa có
    """
    for path in belief:
        if set(path) == white_cells:
            return path
    return None

def sensorless_full_path_search(start_pos, white_cells, N):
    """
    white_cells: danh sách hoặc set các ô trắng trên board
    N: kích thước board (NxN)
    """
    actions = ["Up", "Down", "Left", "Right"]
    # initial belief: robot có thể bắt đầu ở bất kỳ ô trắng nào
    initial_belief = frozenset([tuple([start_pos])])

    frontier = []
    frontier.append(initial_belief)
    explored = set()
    step = 0

    while frontier:
        b = frontier.pop()
        step += 1

        goal_path = goal_test_path(b, set(white_cells))
        if goal_path is not None:
            return list(goal_path), step  # trả về duy nhất path đúng

        explored.add(b)

        for a in actions:
            b_prime = apply_action_to_belief(b, a, N, set(white_cells))
            if b_prime is not None and b_prime not in explored:
                frontier.append(b_prime)

    return None, step  # không tìm được đường đi
