import pygame


class Renderer:
    SCALE = 10

    def __init__(self, display):
        pygame.init()
        self.display = display
        self.window = pygame.display.set_mode(
            (display.WIDTH * self.SCALE, display.HEIGHT * self.SCALE)
        )

    def render(self):
        for y, row in enumerate(self.display.pixels):
            for x, pixel in enumerate(row):
                color = (255, 255, 255) if pixel else (0, 0, 0)
                rect = pygame.Rect(x * self.SCALE, y * self.SCALE, self.SCALE,
                                   self.SCALE)
                pygame.draw.rect(self.window, color, rect)
        pygame.display.flip()
