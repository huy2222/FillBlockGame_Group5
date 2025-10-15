from queue import PriorityQueue
import random
def is_valid(white_cells, N, path, pos):
    return (
        pos not in path
        and pos in white_cells
        and 0 <= pos[0] < N
        and 0 <= pos[1] < N
    )

def distance(a, b):
    return (b[1] - a[1])**2 + (b[0] - a[0])**2

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
        return cost



    



def check(path, white_cells, n):
    cost = 0
    np = path[-1]
    for i in white_cells:
        if i not in path:
            cost += distance(np, i)

    return cost

    


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

def beamsearch(start_pos, white_cells, N, beam_width = 20):
    frontier = [[start_pos]]
    step = 0
    while frontier:
        new_frontier = []
        
        for path in frontier:
            step += 1
            if len(path) == len(white_cells):  # đã đi hết ô trắng
                return path, step
            next_states = generate_next_state(white_cells, N, path)
            new_frontier.extend(next_states)
        
        if not new_frontier:
            break
        
        
        new_frontier.sort(key=lambda x: (x[0], check(x[1], white_cells, N)))
        k = beam_width
        if k > len(new_frontier):
            k = len(new_frontier)
        # lấy top-k
        frontier = [path for cost, path in new_frontier[:k]]
    
    return frontier[0], step
