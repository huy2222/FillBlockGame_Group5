step = 0

def constraint(path, x, y):
    """Kiểm tra xem ô (x, y) có hợp lệ để thêm vào đường đi không"""
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # Nếu ô đã đi qua thì không hợp lệ
    if (x, y) in path:
        return False

    # Nếu là ô đầu tiên thì luôn hợp lệ
    if not path:
        return True

    # ô mới phải kề với ô cuối cùng trong path
    last_x, last_y = path[-1]
    for i in range(4):
        if (last_x + dx[i], last_y + dy[i]) == (x, y):
            return True

    return False


def backtrack(domain_x, path):
    """Thuật toán quay lui để tìm đường đi qua tất cả ô"""
    global step
    step += 1

    # Nếu đi qua hết tất cả ô trắng → thành công
    if len(path) == len(domain_x):
        return path, step

    for (x, y) in domain_x:
        if constraint(path, x, y):
            path.append((x, y))
            result = backtrack(domain_x, path)
            if result is not None:
                return result
            path.pop()  # quay lui

    return None, step


def backtracking_solver(start_pos, white_cells, N):
    """Hàm khởi tạo cho thuật toán backtracking"""
    global step
    step = 0  # reset bộ đếm
    domain_x = list(white_cells)
    path = [start_pos]
    
    result = backtrack(domain_x, path)
    return result
