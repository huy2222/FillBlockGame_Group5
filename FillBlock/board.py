import pygame
from settings import *
import math
from left_panel import *
class Board:
    def __init__(self, screen, N, walkable_cells, start_pos, left_panel = None):
        self.screen = screen
        self.N = N
        self.cell_size = math.ceil(CELL * (12 / N))
        self.grid_pos = (W / 2 - (self.cell_size * N) / 2 + 60, 180)
        self.walkable_cells = set(walkable_cells)

        self.start_pos = start_pos
        self.dot_pos = start_pos
        self.visited = {start_pos}
        self.left_panel = left_panel

    def draw(self):
        for i in range(self.N):
            for j in range(self.N):
                rect = pygame.Rect(
                    self.grid_pos[0] + j * self.cell_size,
                    self.grid_pos[1] + i * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )

                if (i, j) == self.dot_pos:
                    color = DOT
                    pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)  # viền sáng
                elif (i, j) in self.visited:
                    color = ACCENT
                elif (i, j) in self.walkable_cells:
                    color = GRID_DARK
                else:
                    color = WALL

                pygame.draw.rect(self.screen, color, rect, border_radius=4)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1, border_radius=4)

        # DOT tròn giữa ô
        x = self.grid_pos[0] + self.dot_pos[1] * self.cell_size + self.cell_size // 2
        y = self.grid_pos[1] + self.dot_pos[0] * self.cell_size + self.cell_size // 2
        pygame.draw.circle(self.screen, DOT, (x, y), max(6, self.cell_size // 4))

    def move_dot(self, next_pos):
        if next_pos in self.walkable_cells:
            self.dot_pos = next_pos
            self.visited.add(next_pos)

    def follow_path(self, path, delay=1000):
        path_new = []
        for pos in path:
            self.move_dot(pos)
            self.screen.fill(BG)
            self.draw()
            if self.left_panel:
                path_new.append((pos))
                self.left_panel.draw(self.screen, path_new)
            pygame.display.update()
            pygame.time.delay(delay)
        self.dot_pos = self.start_pos
        self.visited = {self.start_pos}
