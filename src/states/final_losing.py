import pygame
import time
import sys

from pygame import MOUSEBUTTONDOWN, KEYDOWN
from pygame.locals import QUIT

from ..utils import get_font, get_gif

BLACK = (0, 0, 0)
COLOR_BACKGROUND = (106, 117, 111)

TITLE = '''КРИСТАЛЛ   РАЗБИТ'''
TEXT_1 = '''ты не оправдал'''
TEXT_2 = '''моих надежд'''

COEF_RESIZE_IMG = 5
SPEED_GIF = 30


class Final_losing:
    def __init__(self, config):
        self.game_config = config
        self.main_surf = pygame.Surface(self.game_config.size_of_screen)

        self.vw = self.game_config.size_of_screen[0] / 100
        self.vh = self.game_config.size_of_screen[1] / 100
        self.vc = min(self.vw, self.vh)

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 15))
        self.pixel_font_bold = get_font("pixel_bold.ttf", int(self.vc * 13))

        self.girl_gif = get_gif("girl_lose.gif")
        self.frame_girl_index = 0

        self.not_clicked = True

        self.cycle_of_game()

        self.game_config.state = "play"

    def resize_image(self, image, sizes=None):
        if sizes:
            return pygame.transform.scale(image, sizes)
        return pygame.transform.scale(
            image,
            (
                image.get_width() * COEF_RESIZE_IMG,
                image.get_height() * COEF_RESIZE_IMG
            )
        )

    def cycle_of_game(self):
        while self.not_clicked:
            for event in pygame.event.get():
                self.check_quit_event(event)
                self.check_tap_anything(event)

            self.draw()
            self.game_config.screen.blit(self.main_surf, (0, 0))
            pygame.display.flip()

            self.game_config.state = "greeting"

    def check_quit_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    def check_tap_anything(self, event):
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.not_clicked = False



    def draw(self):
        self.main_surf.fill(COLOR_BACKGROUND)
        self.draw_text()
        self.draw_girl()

    def draw_text(self):
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

    def draw_girl(self):
        girl = self.girl_gif[self.frame_girl_index // SPEED_GIF]
        girl = self.resize_image(girl)
        self.main_surf.blit(
            girl,
            (95 * self.vw - girl.get_width(), 95 * self.vh - girl.get_height())
        )
        self.frame_girl_index = (self.frame_girl_index + 1) % \
            (len(self.girl_gif) * SPEED_GIF)

# it's state when user lost all lifes
