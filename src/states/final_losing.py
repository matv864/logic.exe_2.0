import pygame
import time

from ..utils import get_font

BLACK = (0, 0, 0)

TITLE = '''YOU    LOSE'''
TEXT = '''Зачем ты расстроил девочку?'''


class Final_losing:
    def __init__(self, config):
        self.game_config = config
        self.main_surf = pygame.Surface(self.game_config.size_of_screen)

        self.vw = self.game_config.size_of_screen[0] / 100
        self.vh = self.game_config.size_of_screen[1] / 100
        self.vc = min(self.vw, self.vh)

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 10))
        self.pixel_font_b = get_font("pixel.ttf", int(self.vc * 15))

        self.draw_screen()

        self.game_config.screen.blit(self.main_surf, (0, 0))
        pygame.display.flip()
        time.sleep(3)
        self.game_config.state = "play"

    def draw_screen(self):
        self.main_surf.fill((255, 255, 255))

        title = self.pixel_font_b.render(TITLE, True, BLACK)
        text = self.pixel_font.render(TEXT, True, BLACK)

        self.main_surf.blit(
            title,
            (20 * self.vw, 35 * self.vh)
        )

        self.main_surf.blit(
            text,
            (20 * self.vw, 50 * self.vh)
        )

# it's state when user lost all lifes
