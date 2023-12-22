import pygame
import time

from ..utils import get_font

BLACK = (0, 0, 0)

TITLE = '''КРИСТАЛЛ   РАЗБИТ'''
TEXT_1 = '''ты не оправдал'''
TEXT_2 = '''моих надежд'''


class Final_losing:
    def __init__(self, config):
        self.game_config = config
        self.main_surf = pygame.Surface(self.game_config.size_of_screen)

        self.vw = self.game_config.size_of_screen[0] / 100
        self.vh = self.game_config.size_of_screen[1] / 100
        self.vc = min(self.vw, self.vh)

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 15))
        self.pixel_font_bold = get_font("pixel_bold.ttf", int(self.vc * 13))

        self.draw_screen()

        self.game_config.screen.blit(self.main_surf, (0, 0))
        pygame.display.flip()
        time.sleep(3)
        self.game_config.state = "play"

    def draw_screen(self):
        self.main_surf.fill((255, 255, 255))

        title = self.pixel_font_bold.render(TITLE, True, BLACK)
        text_1 = self.pixel_font.render(TEXT_1, True, BLACK)
        text_2 = self.pixel_font.render(TEXT_2, True, BLACK)

        self.main_surf.blit(
            title,
            (10 * self.vw, 35 * self.vh)
        )

        self.main_surf.blit(
            text_1,
            (20 * self.vw, 50 * self.vh)
        )
        self.main_surf.blit(
            text_2,
            (20 * self.vw, 60 * self.vh)
        )

# it's state when user lost all lifes
