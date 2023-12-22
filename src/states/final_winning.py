import pygame
import time
import sys

from pygame import MOUSEBUTTONDOWN, KEYDOWN
from pygame.locals import QUIT

from ..utils import save_record, get_font, get_gif

BLACK = (0, 0, 0)

TEXT_OF_TITLE = '''это мой любимый кристалик'''

COLOR_BACKGROUND = (106, 117, 111)

X_POS_INFO = 10
X_POS_BIG_INFO = 5

Y_POS_TITLE = 10
Y_POS_TIME = 30
Y_POS_LIFES = 50
Y_POS_SCORE = 70

COEF_RESIZE_IMG = 5
SPEED_GIF = 20


class Final_winning:
    def __init__(self, config):
        self.game_config = config
        self.main_surf = pygame.Surface(self.game_config.size_of_screen)
        self.not_clicked = True

        self.count_time = int(time.time() - self.game_config.start_time)

        save_record(self.game_config.score)

        self.vw = self.game_config.size_of_screen[0] / 100
        self.vh = self.game_config.size_of_screen[1] / 100
        self.vc = min(self.vw, self.vh)

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 6))
        self.pixel_font_bold = get_font("pixel_bold.ttf", int(self.vc * 10))

        self.girl_gif = get_gif("girl_win.gif")
        self.frame_girl_index = 0

        self.cycle_of_game()

        time.sleep(1)

        self.game_config.level = 1
        self.game_config.update_level_config()
        # self.game_config.state = "greeting"

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

    def generate_text(self):
        self.text_time = f"твоё время прохождения: {self.count_time}"
        self.text_lifes = f"оставшиеся кристаллы: {self.game_config.lifes}"
        self.text_score = f"твой счёт: {self.game_config.score}"

    def draw(self):
        self.main_surf.fill(COLOR_BACKGROUND)
        self.draw_result()
        self.draw_girl()

    def draw_result(self):
        self.generate_text()

        message_title = self.pixel_font_bold.render(TEXT_OF_TITLE, True, BLACK)
        message_time = self.pixel_font.render(self.text_time, True, BLACK)
        message_lifes = self.pixel_font.render(self.text_lifes, True, BLACK)
        message_score = self.pixel_font_bold.render(self.text_score, True, BLACK)

        self.main_surf.blit(
            message_title,
            (X_POS_BIG_INFO * self.vw, Y_POS_TITLE * self.vh)
        )
        self.main_surf.blit(
            message_time,
            (X_POS_INFO * self.vw, Y_POS_TIME * self.vh)
        )
        self.main_surf.blit(
            message_lifes,
            (X_POS_INFO * self.vw, Y_POS_LIFES * self.vh)
        )
        self.main_surf.blit(
            message_score,
            (X_POS_BIG_INFO * self.vw, Y_POS_SCORE * self.vh)
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

# it's state when user win all game
