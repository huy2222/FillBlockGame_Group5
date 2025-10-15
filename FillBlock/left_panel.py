import pygame

class LeftPanel:
    def __init__(self, rect, font, accent_color, text_color, line_height=24):
        self.rect = rect
        self.font = font
        self.accent_color = accent_color
        self.text_color = text_color
        self.line_height = line_height
        self.scroll_offset = 0

    def handle_event(self, event, path_length):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.scroll_offset = max(0, self.scroll_offset - 1)
            elif event.button == 5:
                self.scroll_offset = min(path_length - 1, self.scroll_offset + 1)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.scroll_offset = max(0, self.scroll_offset - 1)
            elif event.key == pygame.K_DOWN:
                self.scroll_offset = min(path_length - 1, self.scroll_offset + 1)

    def draw(self, screen, path):
        # panel nền tối bo tròn
        pygame.draw.rect(screen, (25, 25, 35), self.rect, border_radius=8)
        pygame.draw.rect(screen, self.accent_color, self.rect, 2, border_radius=8)

        if path:
            title = self.font.render("Result Path:", True, self.text_color)
            screen.blit(title, (self.rect[0] + 10, self.rect[1] + 10))

            visible_lines = (self.rect[3] - 50) // self.line_height

            if self.scroll_offset >= len(path) - visible_lines - 1:
                self.scroll_offset = max(0, len(path) - visible_lines)

            
            start = max(0, self.scroll_offset)
            end = min(start + visible_lines, len(path))

            y_offset = 40
            for i, pos in enumerate(path[start:end], start=start):
                step_text = self.font.render(f"{i}: {pos}", True, self.text_color)
                screen.blit(step_text, (self.rect[0] + 10, self.rect[1] + y_offset))
                y_offset += self.line_height
