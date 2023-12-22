import pygame
import time
import sys

from pygame import MOUSEBUTTONDOWN, KEYDOWN
from pygame.locals import QUIT

from ..utils import save_record, get_font

BLACK = (0, 0, 0)

TEXT_OF_TITLE = '''это мой любимый кристалик'''

X_POS_INFO = 10
X_POS_BIG_INFO = 5

Y_POS_TITLE = 10
Y_POS_TIME = 30
Y_POS_LIFES = 50
Y_POS_SCORE = 70


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

        self.cycle_of_game()

        time.sleep(1)

        self.game_config.level = 1
        self.game_config.update_level_config()
        # self.game_config.state = "greeting"

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
        self.generate_text()
        self.main_surf.fill((255, 255, 255))
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

# it's state when user win all game
