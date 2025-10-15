import random

def build_neighbors(n):
    neighbors = {}
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            nb = []
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    nb.append((nx, ny))
            neighbors[(i, j)] = nb
    return neighbors


def dfs(path, visited, neighbors, requestNode):
    if len(path) == requestNode:
        return path

    x, y = path[-1]
    # chọn neighbor còn nhiều lựa chọn trước
    next_moves = [p for p in neighbors[(x, y)] if p not in visited]
    random.shuffle(next_moves)
    next_moves.sort(key=lambda pos: len([q for q in neighbors[pos] if q not in visited]))

    for nx, ny in next_moves:
        visited.add((nx, ny))
        path.append((nx, ny))
        result = dfs(path, visited, neighbors, requestNode)
        if result:
            return result
        # backtrack
        path.pop()
        visited.remove((nx, ny))
    return None


def generateMap(level):
    N = level
    
    requestNode = random.randint(N * N // 2, N * N - N * N // 5)

    neighbors = build_neighbors(N)

    for _ in range(50):  # thử nhiều điểm bắt đầu
        start_pos = (random.randint(0, N - 1), random.randint(0, N - 1))
        path = dfs([start_pos], {start_pos}, neighbors, requestNode)
        if path:
            return (path, start_pos)

    # không tìm thấy đường đi thỏa điều kiện
    return ([], None)
