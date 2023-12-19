import pygame
import time

from ..utils import get_font

BLACK = (0, 0, 0)

START_SCORE = 1000
COEF_SCORE_LIFE = 1000
MAX_LIFES = 3

Y_POS_TEXT = 3

X_POS_LEVEL = 5
X_POS_LIFES = 40
X_POS_SCORE = 80


class Score:
    def __init__(self, config):
        self.game_config = config

        self.time_from_start = 0
        # print(self.game_config.platform_module_size)
        self.vw = self.game_config.score_module_size[0] / 100
        self.vh = self.game_config.score_module_size[1] / 100
        self.vc = min(self.vh, self.vw)
        self.main_surf = pygame.Surface(
            self.game_config.score_module_size,
            pygame.SRCALPHA
        )

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 50))

    def update_time(self):
        time_now = time.time()
        real_time_from_start = time_now - self.game_config.start_time
        self.time_from_start = int(real_time_from_start)

    def update_score(self):
        lost_lifes = MAX_LIFES - self.game_config.lifes
        self.score = START_SCORE - \
            self.time_from_start - \
            COEF_SCORE_LIFE * lost_lifes
        if self.score <= 1:
            self.game_config.state = "losing"
            self.game_config.lifes = 0

    def generate_texts(self):
        self.text_score = f"score: {self.score}"
        self.text_lifes = f"lifes: {self.game_config.lifes}"
        self.text_level = f"level: {self.game_config.level}"

    def draw(self) -> None:
        shade_color = (255, 255, 255, 255)
        self.main_surf.fill(shade_color)
        self.update_time()
        self.update_score()
        self.generate_texts()
        self.draw_texts()

        self.game_config.screen.blit(
            self.main_surf,
            self.game_config.score_module_location,
            special_flags=pygame.BLEND_RGBA_MULT
        )

    def draw_texts(self):
        message_level = self.pixel_font.render(self.text_level, True, BLACK)
        message_lifes = self.pixel_font.render(self.text_lifes, True, BLACK)
        message_score = self.pixel_font.render(self.text_score, True, BLACK)

        self.main_surf.blit(
            message_level,
            (X_POS_LEVEL * self.vw, Y_POS_TEXT * self.vh)
        )

        self.main_surf.blit(
            message_lifes,
            (X_POS_LIFES * self.vw, Y_POS_TEXT * self.vh)
        )

        self.main_surf.blit(
            message_score,
            (X_POS_SCORE * self.vw, Y_POS_TEXT * self.vh)
        )
