import random
import math

def PathCost(path):
    cost = 0
    for i in range(len(path) - 1):
        (x1, y1) = path[i]
        (x2, y2) = path[i+1]
        cost += abs(x1 - x2) + abs(y1 - y2)
    return cost

def SimulatedAnnealing(start_pos, white_cells, level):
    step = 0
    T = 50*len(white_cells)
    alpha = 0.999
    if level == 7:
        T = 200000
        alpha = 0.9995
    Tmin = 1e-5
    state = white_cells.copy()
    random.shuffle(state)
    if state[0] != start_pos:
        idx = state.index(start_pos)
        state[0], state[idx] = state[idx], state[0]

    best_state = state[:]
    best_cost = PathCost(state)

    while T > Tmin:
        step += 1
        i, j = sorted(random.sample(range(1, len(state)), 2))
        neighbor = state[:]
        neighbor[i:j+1] = reversed(neighbor[i:j+1])

        cost_state = PathCost(state)
        cost_neighbor = PathCost(neighbor)
        dE = cost_neighbor - cost_state

        if dE <= 0 or random.random() < math.exp(-dE / T):
            state = neighbor
            cost_state = cost_neighbor

        if cost_state < best_cost:
            best_state, best_cost = state[:], cost_state

        T *= alpha

    return best_state, step
