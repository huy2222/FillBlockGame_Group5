import pygame, sys
import time

from AC3 import ac3_path
from AndOr import and_or_search
from Backtracking import *
from ForwardChecking import ForwardChecking
from Greedy import Greedy
from HillClimbing import hill_climbing_path
from MotPhanNiemTin import MotphanNiemtin
from SensorlessSearch import sensorless_full_path_search
from SimulatedAnnealing import SimulatedAnnealing
from generatemap import generateMap
from board import Board
from settings import *
from button import Button
from DLS import *   
from UCS import *
from left_panel import *
from BFS import *
from Astar import *
from DFS import *
from Beamsearch import *
pygame.init()
screen = pygame.display.set_mode((1440, 760), pygame.RESIZABLE)
pygame.display.set_caption("Block Fill Game")
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()
W, H = screen.get_size()

# Font
FONT_BIG = pygame.font.SysFont("consolas", 64, bold=True)
FONT_LEVEL = pygame.font.SysFont("consolas", 48, bold=True)
FONT_GROUP = pygame.font.SysFont("consolas", 26, bold=True)
FONT_BUTTON = pygame.font.SysFont("consolas", 24)
FONT_PANEL = pygame.font.SysFont("consolas", 22)

# =====================
# BIẾN TOÀN CỤC
board = None
path = []
start_pos = None
result_path = []
level = 7
scroll_offset = 0  # dòng bắt đầu hiển thị
line_height = 24
current_group = None
step  = 0
elapsed_time = 0.0

# =====================
# Khởi tạo LEFT PANEL
# =====================

LEFT_PANEL_RECT = (60, 200, 320, 420)
left_panel = LeftPanel(LEFT_PANEL_RECT, FONT_PANEL, ACCENT, TXT)

# =====================
# HÀM KHỞI TẠO BOARD
# =====================
def create_board(str):
    global level
    if level == 4:
        if str == "Next Level":
            level = 5
        else:
            level = 7
    elif level == 5:
        if str == "Next Level":
            level = 7
        else:
            level = 4
    elif level == 7:
        if str == "Next Level":
            level = 4
        else:
            level = 5
    global board, path, start_pos, result_path
    path, start_pos = generateMap(level)   # sinh map
    board = Board(screen, level, path, start_pos, left_panel)
    result_path = []  # reset kết quả cũ



def PerformanceMeasurement(algorithm, *args):
    start_time = time.perf_counter()
    state_result, step = algorithm(*args)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    return state_result, step, elapsed
# =====================
# thuật toán không có thông tin
# =====================
def run_dfs():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(dfs_solver, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
def run_bfs():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(BFS, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
def run_dls():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(run_dls_model, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("Không tìm được đường đi!")
def run_ucs():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(ucs, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")

# =====================
# thuật toán CÓ THÔNG TIN
# =====================
def run_astar():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(astar_solver, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
def run_greedy():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(Greedy, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")

# =====================
# LocalSearch
# =====================
def run_simulated():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(SimulatedAnnealing, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
    # res, step = SimulatedAnnealing(start_pos, path)
    # print("tar: ", path)
    # print("si", res,' step: ', step)
    # if res:
    #     board.follow_path(res, delay=200)
    # else:
    #     print("không tìm được đường đi!")


def run_hillclimbing():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(hill_climbing_path, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")

def run_beamsearch():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(beamsearch, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
# =====================
# Complex Search
# =====================
def run_andorSearch():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(and_or_search, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
def run_niemtin():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(sensorless_full_path_search, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
def run_motphanniemtin():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(MotphanNiemtin, start_pos, path, level, path[-1])
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
# =====================
# Constraint Search
# =====================
def run_backtracking():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(backtracking_solver, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
def run_forwardchecking():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(ForwardChecking, [start_pos], path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
def run_ac3():
    global result_path, step, elapsed_time
    result_path, step, elapsed_time = PerformanceMeasurement(ac3_path, start_pos, path, level)
    if result_path:
        board.follow_path(result_path, delay=200)
    else:
        print("không tìm được đường đi!")
#các nhóm thuật toán

class AlgoGroup:
    def __init__(self, title, algorithms, x, y):
        self.title = title
        self.algorithms = algorithms
        self.x, self.y = x, y
        self.buttons = [
            Button(x + 60, y + 60 + i * 80, 320, 60, name,
                   color=(100,100,100), hover_color=(170,170,170),
                   font=FONT_BUTTON, action=action)
            for i, (name, action) in enumerate(algorithms)
        ]
        self.header = Button(
            x, y, 330, 50, self.title,
            color=(70, 70, 70), hover_color=(110,110,110),
            font=FONT_GROUP, action=self.toggle
        )
        self.visible = False

    def toggle(self):
        global current_group
        # nếu click lại chính nó thì tắt
        if current_group == self:
            self.visible = False
            current_group = None
        else:
            # ẩn nhóm khác
            for g in groups:
                g.visible = False
            self.visible = True
            current_group = self

    def draw(self, screen):
        if current_group is None or current_group == self:
            self.header.draw(screen)
        if self.visible:
            for b in self.buttons:
                b.draw(screen)

    def handle_event(self, event):
        if current_group is None or current_group == self:
            self.header.handle_event(event)
        if self.visible:
            for b in self.buttons:
                b.handle_event(event)

# =====================
# TẠO NHÓM THUẬT TOÁN
# =====================
right_x = 1040 
top_y = 125    

group_uninformed = AlgoGroup(
    "Tìm kiếm không thông tin",
    [("DFS", run_dfs), ("BFS", run_bfs), ("UCS", run_ucs), ("DLS", run_dls)],
    right_x, top_y
)

group_informed = AlgoGroup(
    "Tìm kiếm có thông tin",
    [("Greedy", run_greedy), ("A*", run_astar)],
    right_x, top_y + 60
)

group_local = AlgoGroup(
    "Local Search",
    [("Hill Climbing", run_hillclimbing), ("Simulated Annealing", run_simulated), ("BeamSearch", run_beamsearch)],
    right_x, top_y + 120
)
group_Complex = AlgoGroup(
    "Complex Search",
    [("AND-OR Search", run_andorSearch),("Belief State", run_niemtin), ("Partial Observation", run_motphanniemtin) ],
    right_x, top_y + 180
)

group_constraint = AlgoGroup(
    "Constraint-Based Search",
    [("Backtracking", run_backtracking), ("Forward Checking", run_forwardchecking), ("AC-3", run_ac3)],
    right_x, top_y + 240
)




groups = [group_uninformed, group_informed, group_local, group_Complex, group_constraint]

# =====================
# NÚT ĐIỀU CHỈNH LEVEL
# =====================
def get_level_text():
    if level == 4:
        return "Level 1 - 4x4"
    elif level == 5:
        return "Level 2 - 5x5"
    else:
        return "Level 3 - 7x7"

#nút level
btn_next = Button(
    W//2 + 380, H - 90, 200, 45, "Next Level",
    color=(100,100,100), hover_color=(170,170,170),
    font=FONT_BUTTON, action=lambda: create_board("Next Level")
)

btn_prev = Button(
    W//2 - 600, H - 90, 200, 45, "Previous Level",
    color=(100,100,100), hover_color=(170,170,170),
    font=FONT_BUTTON, action=lambda: create_board("Previous level")
)

# =====================
# MAIN LOOP
# =====================
create_board("Next Level")  # Khởi tạo level mặc định
def DrawLablePerformance():
    lable_step = FONT_LEVEL.render("Step: ", True, DOT)
    lable_time = FONT_LEVEL.render("Time: ", True, ACCENT)
    screen.blit(lable_step, (30, 70))
    screen.blit(lable_time, (30, 140))
def UpdatePerformance(step = 0, time = 0.0 ):
    step = FONT_LEVEL.render(str(step), True, DOT)
    time = FONT_LEVEL.render(str(round(time, 6)), True, ACCENT)
    screen.blit(step, (200, 70))
    screen.blit(time, (200, 140))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for g in groups:
            g.handle_event(event)
        # Xử lý sự kiện button điều chỉnh level
        btn_prev.handle_event(event)
        btn_next.handle_event(event)
        # Xử lý sự kiện pannel hiện đường đi
        left_panel.handle_event(event, len(result_path))

    # Vẽ nền
    screen.fill(BG)
    # vẽ outline trắng
    title_surface = FONT_BIG.render("BLOCK FILL GAME", True, ACCENT)
    screen.blit(title_surface, (W//2 - title_surface.get_width()//2, 30))
    # Vẽ board
    board.draw()
    DrawLablePerformance()
    UpdatePerformance(step, elapsed_time)

    # Vẽ panel trái hiển thị đường đi
    left_panel.draw(screen, result_path)

    # Nhóm thuật toán
    for g in groups:
        g.draw(screen)
     # Nút level
    btn_prev.draw(screen)
    btn_next.draw(screen)
    
    # Update màn hình
    pygame.display.flip()
    clock.tick(30)
